#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import fields

install_requires = [
    'django>=1.2',
    'pytest',
]

readme = open('./fields/README.md', 'r')
README_TEXT = readme.read()
readme.close()

setup(name='django_compressfield',
      url='https://github.com/valdergallo/django-compressfield',
      author="valdergallo",
      author_email='valdergallo@gmail.com',
      keywords='Django Compress Field',
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
      version=fields.__version__,
      install_requires=install_requires,
      packages=find_packages(where='.',
                             exclude=('*test*', '*example*')),
)
