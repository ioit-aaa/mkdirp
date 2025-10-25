from setuptools import setup, find_packages

setup(
    name="mkdirp",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mkdirp=mkdirp.cli:main",
        ],
    },
    author="NapCatDev",
    license="GPL-3.0",
    python_requires=">=3.6",
)