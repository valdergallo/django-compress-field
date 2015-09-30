# -*- coding: utf-8 -*-
from .fieldfiles import ZipCompressFieldFile
from django.db import models


class ZipFileField(models.FileField):
    """
    ZipField - auto zip content after file was saved on server
    """
    attr_class = ZipCompressFieldFile


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^compress_field\.models\.(ZipFileField)"])
except ImportError:
    pass
