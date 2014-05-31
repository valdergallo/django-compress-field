# -*- coding: utf-8 -*-
import zipfile
import os
from .base import CompressFieldFile
from django.conf import settings
from django.core.files.base import File


class ZipCompressFieldFile(CompressFieldFile):
    compress_ext = 'zip'

    def compress_content(self, delete_old_file=True):
        """
        Method to change for new implementations
        """
        compress_file_fullname = os.path.join(settings.MEDIA_ROOT, self.compress_name)

        if self.is_compressed:
            return 'File alredy compress'

        in_memory_zip = file(compress_file_fullname, 'w')
        ziped = zipfile.ZipFile(in_memory_zip, "w", zipfile.ZIP_DEFLATED)
        ziped.write(self.file.name)
        ziped.close()

        return ziped
