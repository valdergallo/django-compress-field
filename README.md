Django Compress Storage
=======================

[![Build Status](https://travis-ci.org/valdergallo/django-compress-storage.png?branch=master)](https://travis-ci.org/valdergallo/django-compress-storage)
[![Coverage Status](https://coveralls.io/repos/valdergallo/django-compress-storage/badge.png)](https://coveralls.io/r/valdergallo/django-compress-storage)


Custom Field for Django that auto compact file uploaded


Features
========

- Compress FileUpload storage file with Zip
- Delete onde file that was compressed on zip
- Suport for South Migrations
- Suport Django 1.2+
- Celery support - async compress file with Celery


Usage
=====

```python

# example model.py

from django.db import models
from compress_storage import ZipFileField

class MyContent(models.Model):
    name = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now=True)
    upload_file = ZipFileField(upload_to='mycontent/')

    def __unicode__(self):
        return self.name

```

Shell
=====

```python

>>> from example.core import MyContent
>>> m = MyContent.objects.get(id=2)
>>> m.upload_file
<ZipCompressFieldFile: mycontent/test.txt>
>>> m.upload_file.compress()
>>> m.upload_file
<ZipCompressFieldFile: mycontent/test.zip>
```

Developer
=========

```bash
# download code
git clone https://github.com/valdergallo/django-compress-storage

# install developer packages
setup.py develop

# test project
setup.py test

#clean extra content
setup.py clean

```


