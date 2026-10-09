import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


def get_bayer_masks(n_rows, n_cols):

    print('Hello, world')
    """
    :param n_rows: `int`, number of rows
    :param n_cols: `int`, number of columns

    :return:
        `np.array` of shape `(n_rows, n_cols, 3)` and dtype `np.bool_`
        containing red, green and blue Bayer masks
    """


def get_colored_img(raw_img):
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
    """
    :param colored_img:
        `np.array` of shape `(n_rows, n_cols, 3)` and dtype `np.uint8`,
        colored image

    :return:
        `np.array` of shape `(n_rows, n_cols)` and dtype `np.uint8`,
        raw image as captured by camera
    """


def bilinear_interpolation(raw_img):
    """
    :param raw_img:
        `np.array` of shape `(n_rows, n_cols)` and dtype `np.uint8`,
        raw image

    :return:
        `np.array` of shape `(n_rows, n_cols, 3)`, and dtype `np.uint8`,
        result of bilinear interpolation
    """


def improved_interpolation(raw_img):
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
