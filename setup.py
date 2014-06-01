#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

os.environ['DJANGO_SETTINGS_MODULE'] = 'example.test_settings'

import compress_storage

install_requires = [
    'django>=1.2',
]

readme = open('README.md', 'r')
README_TEXT = readme.read()
readme.close()


setup(name='django-compress-storage',
      url='https://github.com/valdergallo/django-compress-storage',
      author="valdergallo",
      author_email='valdergallo@gmail.com',
      keywords='Django Compress Field Zip Tar GZip',
      description='Automantic compress fiels after upload',
      license='Apache License',
      long_description=README_TEXT,
      classifiers=[
          'Framework :: Django',
          'Operating System :: OS Independent',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
      ],
      include_package_data=True,
      version=compress_storage.__version__,
      install_requires=install_requires,
      test_suite = "runtest.runtests",
      packages=find_packages(where='.',
                             exclude=('*test*', '*example*', 'runtest')),
)
