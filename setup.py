#!/usr/bin/env python3

from setuptools import setup

setup(
    name="libdecsync",
    version="1.3.1",
    author="Aldo Gunsing",
    author_email="dev@aldogunsing.nl",
    url="https://github.com/39aldo39/libdecsync-bindings-python3",
    description="Python3 bindings for libdecsync",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=["decsync"],
    license="LGPLv2+",
    packages=["libdecsync"],
    package_data={"libdecsync":["libs/*"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        "Intended Audience :: Developers"
    ]
)
