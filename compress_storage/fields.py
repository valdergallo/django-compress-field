# -*- coding: utf-8 -*-
from .fieldfiles import ZipCompressFieldFile
from django.db.models import FileField


class ZipField(FileField):
    """
    ZipField - auto zip content after file was saved on server
    """
    attr_class = ZipCompressFieldFile
