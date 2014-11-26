#!/usr/bin/env python

from setuptools import setup

packages = ['Django<=1.4', 'BeautifulSoup4', 'south', 'markdown']

setup(
    name='blog',
    version='0.2',
    description='Simple blog built with Django, hosted on Openshift',
    author='Gareth M',
    install_requires=packages,
)