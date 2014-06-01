# -*- coding: utf-8 -*-
from zipfile import ZipFile, ZIP_DEFLATED
import os
import sys
from .base import CompressFieldFile
from django.conf import settings


class ZipCompressFieldFile(CompressFieldFile):
    compress_ext = 'zip'

    def compress_content(self):
        compress_file_fullname = os.path.join(settings.MEDIA_ROOT, self.compress_name)

        # to work with py2.6 or lower
        if sys.version_info < (2, 7):
            compress_file_fullname = file(compress_file_fullname, 'w')

        if self.is_compressed:
            return 'File alredy compress'

        ziped = ZipFile(compress_file_fullname, 'w', ZIP_DEFLATED)
        ziped.write(str(self.file.name))
        ziped.close()

        return ziped
