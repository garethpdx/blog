#!/usr/bin/env python

from setuptools import setup

packages = ['Django==1.7', 'BeautifulSoup4', 'markdown',
            'django-markup-deprecated']

setup(
    name='blog',
    version='0.3.3',
    description='Simple blog built with Django, hosted on Openshift',
    author='Gareth M',
    install_requires=packages,
)
