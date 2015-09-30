#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

os.environ['DJANGO_SETTINGS_MODULE'] = 'example.test_settings'

import compress_field

install_requires = [
    'django>=1.2',
]


def readme():
    try:
        os.system('pandoc --from=markdown --to=rst README.md -o README.rst')
        with open('README.rst') as f:
            return f.read()
    except:
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
          'Programming Language :: Python :: 3.3',
      ],
      include_package_data=True,
      version=compress_field.__version__,
      install_requires=install_requires,
      test_suite="runtest.runtests",
      packages=find_packages(where='.',
                             exclude=('*test*', '*example*', 'runtest')),
)
