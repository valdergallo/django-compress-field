from django.db import models
from compress_fields import ZipField


class MyContent(models.Model):
    name = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now=True)
    upload_file = ZipField(upload_to='mycontent/')

    def __unicode__(self):
        return self.name
