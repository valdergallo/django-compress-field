#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import pytest

import fields

install_requires = [
    'django>=1.2',
    'pytest',
]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['compress_field']
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        errno = pytest.main(self.test_args)
        sys.exit(errno)


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
      cmdclass={'test': PyTest},
      packages=find_packages(where='.',
                             exclude=('*test*', '*example*')),
)
