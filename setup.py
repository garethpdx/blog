#!/usr/bin/env python

from setuptools import setup

packages = ['Django<=1.6',]

setup(
    name='blog',
    version='0.1',
    description='OpenShift App',
    author='Gareth',
    author_email='example@example.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=packages,
)
