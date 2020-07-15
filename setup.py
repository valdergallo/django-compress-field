#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

import compress_field

install_requires = [
    'django>=1.2',
]

tests_requires = [
    'django>=1.2',
    'pytest==5.4.3',
    'pytest-runner==5.2',
    'pytest-django==3.9.0',
    'pytest-cov==2.10.0',
]


setup(name='django-compress-field',
      url='https://github.com/valdergallo/django-compress-field',
      download_url='https://github.com/valdergallo/django-compress-field/tarball/v%s/' % compress_field.__version__,
      author="valdergallo",
      author_email='valdergallo@gmail.com',
      keywords=['django', 'compress', 'field', 'zip', 'tar', 'gzip'],
      description='Automantic compress files after upload',
      license='FREEBSD',
      classifiers=[
          'Framework :: Django',
          'Operating System :: OS Independent',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
      ],
      include_package_data=True,
      version=compress_field.__version__,
      install_requires=install_requires,
      tests_require=tests_requires,
      setup_requires=['pytest-runner'],
      platforms='any',
      packages=[
            'compress_field'
        ]
      )
