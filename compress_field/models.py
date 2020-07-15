# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .fieldfiles import ZipCompressFieldFile
from django.db import models


class ZipFileField(models.FileField):
    """
    ZipField - auto zip content after file was saved on server
    """

    attr_class = ZipCompressFieldFile

    def south_field_triple(self):
        try:
            from south.modelsinspector import introspector

            cls_name = "{0}.{1}".format(
                self.__class__.__module__, self.__class__.__name__
            )
            args, kwargs = introspector(self)
            return cls_name, args, kwargs
        except ImportError:
            pass


try:
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([], ["^compress_field\.models\.(ZipFileField)"])
except ImportError:
    pass
