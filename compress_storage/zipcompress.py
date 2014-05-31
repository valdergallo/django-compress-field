# -*- coding: utf-8 -*-
from .base import FileCompressorField

class ZipField(FileCompressorField):
    """
    ZipField - auto zip content after file was saved on server
    """
    compress_ext = 'zip'
