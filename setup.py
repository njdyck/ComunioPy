#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from distutils.core import setup

long_description = open('README.md', 'rt').read(),
if os.path.exists('README.txt'):
    long_description = open('README.txt').read(),
        
setup(
    name = 'ComunioPy',
    packages = ['ComunioPy'],
    version = '1.2',
    description = 'API for comunio',
    license = 'MIT',
    author = 'Javier Corbín',
    author_email = 'javi.corbin@gmail.com',
    url = 'https://github.com/jotacor/ComunioPy',
    download_url = 'https://github.com/jotacor/ComunioPy/archive/v1.2.tar.gz', 
    keywords = ['comunio', 'API'],
    classifiers = [],
)
