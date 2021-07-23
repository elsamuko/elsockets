#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='elsockets',
    version='0.1.0',
    description="Python websockets server",
    author="elsamuko",
    license="MIT license",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "elsockets = elsockets.elsockets:main",
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
