import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


def get_bayer_masks(n_rows, n_cols):
    template_r = np.array([[False, True],
                          [False, False]])
    template_g = np.array([[True, False],
                          [False, True]])
    template_b = np.array([[False, False],
                          [True, False]])
    bayer = np.tile(np.stack([template_r, template_g, template_b], axis=2), ((n_rows + 1)// 2, (n_cols + 1) // 2, 1))
    return bayer[:n_rows, :n_cols, :]

    """
    :param n_rows: `int`, number of rows
    :param n_cols: `int`, number of columns 

    :return:
        `np.array` of shape `(n_rows, n_cols, 3)` and dtype `np.bool_`
        containing red, green and blue Bayer masks
    """


def get_colored_img(raw_img):
    mask = get_bayer_masks(raw_img.shape[0], raw_img.shape[1])
    return np.where(mask, np.repeat(raw_img[:, :, None], 3, axis=2), 0)



    """
    :param raw_img:
        `np.array` of shape `(n_rows, n_cols)` and dtype `np.uint8`,
        raw image

    :return:
        `np.array` of shape `(n_rows, n_cols, 3)` and dtype `np.uint8`,
        each channel contains known color values or zeros
        depending on Bayer masks
    """


def get_raw_img(colored_img):
    mask = get_bayer_masks(colored_img.shape[0], colored_img.shape[1])
    return np.where(mask[:, :, 0], colored_img[:, :, 0], 0) + \
             np.where(mask[:, :, 1], colored_img[:, :, 1], 0) + \
             np.where(mask[:, :, 2], colored_img[:, :, 2], 0)


    """
    :param colored_img:
        `np.array` of shape `(n_rows, n_cols, 3)` and dtype `np.uint8`,
        colored image

    :return:
        `np.array` of shape `(n_rows, n_cols)` and dtype `np.uint8`,
        raw image as captured by camera
    """


def bilinear_interpolation(raw_img):
    mask = get_bayer_masks(raw_img.shape[0], raw_img.shape[1])
    image = get_colored_img(raw_img)
    colors = []

    for i in range(0, 3):
        color = np.pad(image[:, :, i],1, mode='constant')
        norm = np.pad(mask[:, :, i].astype(int), 1, 'constant', constant_values=(0))
        color = sliding_window_view(color, (3, 3))
        count = np.sum(sliding_window_view(norm, (3, 3)), axis=(2, 3))
        color = np.where(~mask[:, :, i], np.sum(color, axis=(2, 3)) / count, image[:, :, i])
        colors.append(np.round(color).astype('uint8'))

    return np.stack(colors, axis=2)






    """
    :param raw_img:
        `np.array` of shape `(n_rows, n_cols)` and dtype `np.uint8`,
        raw image

    :return:
        `np.array` of shape `(n_rows, n_cols, 3)`, and dtype `np.uint8`,
        result of bilinear interpolation
    """


def improved_interpolation(raw_img):
    mask = get_bayer_masks(raw_img.shape[0], raw_img.shape[1])
    image = get_colored_img(raw_img) / 255

    green_channel = np.pad(image[:, :, 1], 2, mode='constant')
    green_template = np.pad(mask[:, :, 1], 2, mode='constant', constant_values=(False))
    red_channel = np.pad(image[:, :, 0], 2, mode='constant')
    red_template = np.pad(mask[:, :, 0], 2, mode='constant', constant_values=(False))
    blue_channel = np.pad(image[:, :, 2], 2, mode='constant')
    blue_template = np.pad(mask[:, :, 2], 2, mode='constant', constant_values=(False))



    def channel(mask):
        slid = sliding_window_view(raw_img / 255, (5, 5))
        return np.clip(np.pad((slid * mask).sum(axis=(2, 3)), 4, mode='constant'), 0, 1)



    green_on_red_mask = (1/8) * np.array([[0, 0, -1, 0, 0],
                                          [0, 0, 2, 0, 0],
                                          [-1, 2, 4, 2, -1],
                                          [0, 0, 2, 0, 0],
                                          [0, 0, -1, 0, 0]])

    green_channel_on_red = channel(green_on_red_mask)
    green_channel = np.where(red_template, green_channel_on_red, green_channel)
    green_channel = np.where(blue_template, green_channel_on_red, green_channel)




    red_on_green_mask_1 = (1/8) * np.array([[0, 0, 1/2, 0, 0],
                                            [0, -1, 0, -1, 0],
                                            [-1, 4, 5, 4, -1],
                                            [0, -1, 0, -1, 0],
                                            [0, 0, 1/2, 0, 0]])

    red_channel_on_green_1 =  channel(red_on_green_mask_1)
    green_template_1 = green_template.copy()
    green_template_2 = green_template.copy()
    green_template_1[1::2] *= False
    green_template_2[0::2] *= False
    red_channel = np.where(green_template_1, red_channel_on_green_1, red_channel)
    blue_channel = np.where(green_template_2, red_channel_on_green_1, blue_channel)



    red_on_green_mask_2 = (1/8) * np.array([[0, 0, -1, 0, 0],
                                            [0, -1, 4, -1, 0],
                                            [1/2, 0, 5, 0, 1/2],
                                            [0, -1, 4, -1, 0],
                                            [0, 0, -1, 0, 0]])

    red_channel_on_green_2 =  channel(red_on_green_mask_2)
    red_channel = np.where(green_template_2, red_channel_on_green_2, red_channel)
    blue_channel = np.where(green_template_1, red_channel_on_green_2, blue_channel)


    red_on_blue_mask = (1/8) * np.array([[0, 0, -3/2, 0, 0],
                                         [0, 2, 0, 2, 0],
                                         [-3/2, 0, 6, 0, -3/2],
                                         [0, 2, 0, 2, 0],
                                         [0, 0, -3/2, 0, 0]])

    red_channel_on_blue = channel(red_on_blue_mask)
    red_channel = np.where(blue_template, red_channel_on_blue, red_channel)
    blue_channel = np.where(red_template, red_channel_on_blue, blue_channel)



    return ((np.stack([red_channel[2:-2, 2:-2], green_channel[2:-2, 2:-2], blue_channel[2:-2, 2:-2]], axis=2) * 255).astype('uint8'))





    """
    :param raw_img:
        `np.array` of shape `(n_rows, n_cols)` and dtype `np.uint8`, raw image

    :return:
        `np.array` of shape `(n_rows, n_cols, 3)` and dtype `np.uint8`,
        result of improved interpolation
    """


def compute_psnr(img_pred, img_gt):
    """
    :param img_pred:
        `np.array` of shape `(n_rows, n_cols, 3)` and dtype `np.uint8`,
        predicted image
    :param img_gt:
        `np.array` of shape `(n_rows, n_cols, 3)` and dtype `np.uint8`,
        ground truth image

    :return:
        `float`, PSNR metric
    """
    

if __name__ == "__main__":
    import common

    for img_name, img_raw, img_gt in common.get_test_images():
        print(f"Processing {img_name}...")
        img_bilinear = bilinear_interpolation(img_raw)
        img_improved = improved_interpolation(img_raw)
        if img_bilinear is not None:
            print("PSNR (bilinear):", compute_psnr(img_bilinear, img_gt))
            common.save_image(f"imgs_bilinear/{img_name}", img_bilinear)
        if img_improved is not None:
            print("PSNR (improved):", compute_psnr(img_improved, img_gt))
            common.save_image(f"imgs_improved/{img_name}", img_improved)
        print()








