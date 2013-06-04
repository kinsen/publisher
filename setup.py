#*_* coding=utf8 *_*

"""
描述：项目安装脚本。
作者：Kong
"""

import os
import setuptools
import sys

requirements = []

setuptools.setup(
    name="publisher",
    version="2013.6",
    author="Kong",
    description="The web site of dash manage.",
    packages=setuptools.find_packages(exclude=['tests','bin']),
    scripts = ['bin/publisher'],
    install_requires=requirements,
)
