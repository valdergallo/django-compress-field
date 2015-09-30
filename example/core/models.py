from django.db import models
from compress_field import ZipFileField


class MyContent(models.Model):
    name = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now=True)
    upload_file = ZipFileField(upload_to='mycontent/2014/06/03/')

    def __unicode__(self):
        return self.name
