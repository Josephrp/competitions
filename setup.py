# coding=utf-8
# Copyright 2022 Hugging Face Inc
#
# Lint as: python3
# pylint: enable=line-too-long
"""Hugging Face Competitions
"""
from setuptools import find_packages, setup


with open("README.md") as f:
    long_description = f.read()

QUALITY_REQUIRE = [
    "black~=22.0",
    "isort==5.8.0",
    "flake8==3.9.2",
    "mypy==0.901",
]

TEST_REQUIRE = ["pytest", "pytest-cov"]

EXTRAS_REQUIRE = {
    "dev": QUALITY_REQUIRE,
    "quality": QUALITY_REQUIRE,
    "test": TEST_REQUIRE,
    "docs": [
        "recommonmark",
        "sphinx==3.1.2",
        "sphinx-markdown-tables",
        "sphinx-rtd-theme==0.4.3",
        "sphinx-copybutton",
    ],
}

with open("requirements.txt") as f:
    INSTALL_REQUIRES = f.read().splitlines()

setup(
    name="competitions",
    description="Hugging Face Competitions",
    long_description=long_description,
    author="HuggingFace Inc.",
    url="https://github.com/huggingface/competitions",
    download_url="https://github.com/huggingface/competitions/tags",
    packages=find_packages("."),
    entry_points={"console_scripts": ["competitions=competitions.cli.competitions:main"]},
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="huggingface competitions machine learning ai nlp",
)