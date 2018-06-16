#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import setup

package_name = 'mtprotoproxy'


def get_version(package=package_name):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search(r'__version__ = [\'\"]([^\'\"]+)[\'\"]', init_py).group(1)


def get_packages(package=package_name):
    return [dirpath for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_description(path='README.md'):
    try:
        from pypandoc import convert
        return convert(path, 'rst')
    except ImportError:
        with open(path) as f:
            return f.read()


setup(
    name=package_name,
    version=get_version(),
    url='https://github.com/alexbers/mtprotoproxy',
    license='MIT',
    description='Async mtproto proxy for Telegram.',
    long_description=get_description(),
    author='Alexander Bersenev',
    author_email='bay@hackerdom.ru',
    packages=get_packages(),
    extras_require={
        'pyaes': [
            'pyaes',
        ],
        'pycryptodome': [
            'pycryptodome'
        ],
        'pycrypto': [
            'pycrypto'
        ],
        'uvloop': [
            'uvloop',
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: System Administrators',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'mtprotoproxy=mtprotoproxy.cli:run',
        ]
    }
)
