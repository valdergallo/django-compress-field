Django Compress Storage
=======================

Custom Storage for Django that auto compact file upload


Features
========

- Compress FileUpload storage file with Zip
- Delete onde file that was compressed on zip
- Suport for South Migrations
- Suport Django 1.2+


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


