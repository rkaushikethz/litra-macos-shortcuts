"""
Setup script for Litra Glow macOS Shortcuts Controller

Author: RKaushik
License: MIT
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="litra-macos-shortcuts",
    version="1.0.0",
    author="RKaushik",
    description="Control Logitech Litra Glow light from macOS Shortcuts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rkaushikethz/litra-macos-shortcuts",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Home Automation",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: MacOS :: MacOS X",
    ],
    python_requires=">=3.8",
    install_requires=[
        "hidapi>=0.14.0",
    ],
    entry_points={
        "console_scripts": [
            "litra-control=litra_control:main",
        ],
    },
)
