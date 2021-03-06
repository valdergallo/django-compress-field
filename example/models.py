from __future__ import absolute_import, unicode_literals
from django.db import models
from compress_field.models import ZipFileField


class MyContent(models.Model):
    name = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now=True)
    upload_file = ZipFileField(upload_to='mycontent/2014/06/03/')

    def __str__(self):
        return self.name
