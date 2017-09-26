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
    'pytest==3.0.2',
    'pytest-django==2.9.1',
    'pytest-cov==2.3.1',
]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['compress_field', 'tests', '--cov=compress_field', '-vrsx']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def readme():
    try:
        os.system('pandoc --from=markdown --to=rst README.md -o README.rst')
        with open('README.rst') as f:
            return f.read()
    except Exception:
        return 'Automantic compress files after upload'


setup(name='django-compress-field',
      url='https://github.com/valdergallo/django-compress-field',
      download_url='https://github.com/valdergallo/django-compress-field/tarball/v%s/' % compress_field.__version__,
      author="valdergallo",
      author_email='valdergallo@gmail.com',
      keywords=['django', 'compress', 'field', 'zip', 'tar', 'gzip'],
      description='Automantic compress files after upload',
      long_description=readme(),
      license='FREEBSD',
      classifiers=[
          'Framework :: Django',
          'Operating System :: OS Independent',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.6',
      ],
      include_package_data=True,
      version=compress_field.__version__,
      install_requires=install_requires,
      tests_require=tests_requires,
      cmdclass={'test': PyTest},
      platforms='any',
      packages=[
            'compress_field'
        ]
      )
