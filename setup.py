from setuptools import setup, find_packages

setup(
    name="CloneBO",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "torch",
        "tqdm",
        "transformers",
        "huggingface_hub",
        "hydra-core",
        "omegaconf",
        "wandb",
        "biopython",
        "termcolor",
        "pytorch-lightning",
        "scipy",
        "matplotlib",
        "p_tqdm",
        "transformers",
        "simplejson",
        "pydantic<2",
        "sru",
        "iglm",
        "pyarrow",
        "scikit-learn"
        r"abnumber @ git+https://github.com/prihoda/AbNumber.git@e5d8e2bf89b8ae28b9f435f3061f3ad3bdd102fb#egg=abnumber",
    ],
    python_requires="==3.12",
)
