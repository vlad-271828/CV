set -o xtrace

setup_root() {
    apt-get install -qq -y \
        ffmpeg             \
        git                \
        python3-pip        \
        python3-tk         \
        ;

    ## Unpinned
    # python3 -m pip install -qq             \
    #     --no-cache-dir                     \
    #     albumentations                     \
    #     albumentations_experimental        \
    #     imgaug                             \
    #     kornia                             \
    #     lightning[extra]                   \
    #     matplotlib                         \
    #     moviepy                            \
    #     opencv-python-headless             \
    #     pandas                             \
    #     pytest                             \
    #     scikit-image                       \
    #     scikit-learn                       \
    #     timm                               \
    #     torch                              \
    #     torchvision                        \
    #     einops                             \
    #     ;

    ## Pinned
    python3 -m pip install -qq             \
        --no-cache-dir                     \
        aiohappyeyeballs==2.7.1            \
        aiohttp==3.14.3                    \
        aiosignal==1.4.0                   \
        albucore==0.0.24                   \
        albumentations==2.0.8              \
        albumentations-experimental==0.0.1 \
        annotated-types==0.8.0             \
        antlr4-python3-runtime==4.9.3      \
        anyio==4.14.2                      \
        attrs==26.1.0                      \
        bitsandbytes==0.50.2               \
        certifi==2026.7.22                 \
        click==8.5.0                       \
        cloudpickle==3.1.2                 \
        contourpy==1.3.3                   \
        cuda-bindings==13.3.1              \
        cuda-pathfinder==1.8.0             \
        cuda-toolkit==13.0.3.0             \
        cycler==0.12.1                     \
        decorator==5.3.1                   \
        docstring_parser==0.18.0           \
        einops==0.8.2                      \
        filelock==3.32.5                   \
        fonttools==4.64.0                  \
        frozenlist==1.8.0                  \
        fsspec==2026.7.0                   \
        h11==0.16.0                        \
        hf-xet==1.6.0                      \
        httpcore==1.0.9                    \
        httpx==0.28.1                      \
        huggingface_hub==1.29.0            \
        hydra-core==1.3.6                  \
        idna==3.19                         \
        ImageIO==2.37.4                    \
        imageio-ffmpeg==0.6.0              \
        imgaug==0.4.0                      \
        iniconfig==2.3.0                   \
        Jinja2==3.1.6                      \
        joblib==1.6.0                      \
        jsonargparse==4.52.0               \
        jsonnet==0.22.0                    \
        kiwisolver==1.5.1                  \
        kornia==0.8.3                      \
        kornia_rs==0.1.14                  \
        lazy-loader==0.5                   \
        lightning==2.6.5                   \
        lightning-utilities==0.15.3        \
        markdown-it-py==4.2.0              \
        MarkupSafe==3.0.3                  \
        matplotlib==3.11.1                 \
        mdurl==0.1.2                       \
        moviepy==2.2.1                     \
        mpmath==1.3.0                      \
        multidict==6.7.1                   \
        narwhals==2.25.0                   \
        networkx==3.6.1                    \
        numpy==2.5.2                       \
        nvidia-cublas==13.1.1.3            \
        nvidia-cuda-cupti==13.0.85         \
        nvidia-cuda-nvrtc==13.0.88         \
        nvidia-cuda-runtime==13.0.96       \
        nvidia-cudnn-cu13==9.24.0.43       \
        nvidia-cufft==12.0.0.61            \
        nvidia-cufile==1.15.1.6            \
        nvidia-curand==10.4.0.35           \
        nvidia-cusolver==12.0.4.66         \
        nvidia-cusparse==12.6.3.3          \
        nvidia-cusparselt-cu13==0.8.1      \
        nvidia-nccl-cu13==2.30.7           \
        nvidia-nvjitlink==13.3.33          \
        nvidia-nvshmem-cu13==3.4.5         \
        nvidia-nvtx==13.0.85               \
        omegaconf==2.3.1                   \
        opencv-python==5.0.0.93            \
        opencv-python-headless==5.0.0.93   \
        packaging==26.3                    \
        pandas==3.0.5                      \
        pillow==11.3.0                     \
        pluggy==1.6.0                      \
        proglog==0.1.12                    \
        propcache==0.5.2                   \
        protobuf==7.36.1                   \
        pydantic==2.13.5                   \
        pydantic_core==2.46.5              \
        Pygments==2.21.0                   \
        pyparsing==3.3.2                   \
        pytest==9.1.1                      \
        python-dateutil==2.9.0.post0       \
        python-dotenv==1.2.3               \
        pytorch-lightning==2.6.5           \
        PyYAML==6.0.3                      \
        rich==14.3.4                       \
        safetensors==0.8.0                 \
        scikit-image==0.26.0               \
        scikit-learn==1.9.0                \
        scipy==1.18.1                      \
        setuptools==84.0.0                 \
        shapely==2.1.2                     \
        simsimd==6.5.16                    \
        six==1.17.0                        \
        stringzilla==5.1.2                 \
        sympy==1.14.0                      \
        tensorboardX==2.6.5                \
        threadpoolctl==3.6.0               \
        tifffile==2026.8.23                \
        timm==1.0.29                       \
        torch==2.14.0                      \
        torchmetrics==1.9.0                \
        torchvision==0.29.0                \
        tqdm==4.70.0                       \
        triton==3.8.0                      \
        typeshed_client==2.13.0            \
        typing-inspection==0.4.4           \
        typing_extensions==4.16.0          \
        wheel==0.42.0                      \
        yarl==1.24.5                       \
        ;
}

setup_checker() {
    python3 --version # Python 3.12.3
    python3 -m pip freeze # see list above
    python3 -c 'import matplotlib.pyplot'
}

"$@"