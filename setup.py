#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='MonMonMon',
    author='Charles Nelson',
    author_email='cnelsonsic+monmonmon@gmail.com',
    version='0.1.0',
    description='A web-based monster capturing/training/fighting game.',
    license='GNU Affero General Public License v3',
    long_description=__doc__,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Topic :: Games/Entertainment :: Role-Playing',
    ],
    include_package_data=True,
    zip_safe=False,
    setup_requires=['nose>=1.0'],
    install_requires=['Flask']
)
