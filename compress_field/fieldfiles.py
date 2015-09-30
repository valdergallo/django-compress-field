# -*- coding: utf-8 -*-
import zipfile
import sys
from .base import CompressFieldFile
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except ImportError:
    compression = zipfile.ZIP_STORED


class ZipCompressFieldFile(CompressFieldFile):
    compress_ext = 'zip'

    def compress_content(self):
        compress_file_fullname = self.compress_full_name

        # to work with py2.6 or lower
        if sys.version_info < (2, 7):
            compress_file_fullname = open(compress_file_fullname, 'w+b')

        if not zipfile.is_zipfile(self.file.name):
            ziped = zipfile.ZipFile(compress_file_fullname, 'w', compression=compression)
            ziped.write(self.file.name, self.base_name)
            ziped.close()
            return ziped
