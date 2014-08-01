#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

#import devent

setup(
    name = 'devent',
    version = '0.0.1',
    zip_safe = False,
    author = 'Mocker',
    author_email = 'Zuckerwooo@gmail.com',
    license = 'MIT',
    platforms = ['any'],
    packages = ['devent'],
    install_requires = ['gevent'],
    keywords = 'event, watcher',
    url = 'https://github.com/zuckonit/devent',
    description = 'dynamic event watcher',
)
