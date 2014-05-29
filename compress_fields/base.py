# -*- coding: utf-8 -*-
try:
    from celery.task import task
except ImportError:
    task = None

import zipfile
import os

from django.db.models import FileField
from django.conf import settings

FILE_COMPRESS_DELETE_OLD_FILE = getattr(settings, 'FILE_COMPRESS_DELETE_OLD_FILE', True)


class FileCompressorField(FileField):
    compress_ext = 'zip'

    def get_compress_name(self):
        basename, ext = os.path.extsep(self.name)
        return os.path.join(basename, self.compress_ext)

    def generate_compress_filename_with_path(self):
        return os.path.join(self.get_directory_name(), self.get_compress_name())

    def compress_content(self, delete_old_file=True):
        """
        Method to change for new implementations
        """
        in_memory_zip = file(self.generate_compress_filename_with_path(), 'w')
        ziped = zipfile.ZipFile(in_memory_zip, "w", zipfile.ZIP_DEFLATED)
        ziped.write(self.name)
        ziped.close()

        self.save_compress_content(ziped, delete_old_file)
        return ziped

    def save_compress_content(self, file_content, delete_old_file=True):
        if delete_old_file:  # remove old file
            self.storage.delete(self.name)

        # save zipfile on database
        return super(FileField, self).save(self.get_compress_name(), file_content)

    def compress_file(self, async=True, delete_old_file=True):
        if async and task:
            file_content = task(self.compress_content).delay(delete_old_file=delete_old_file)
        else:
            file_content = self.compress_content(delete_old_file=delete_old_file)

        return file_content

    def save(self, name, content, save=True):
        super(FileCompressorField, self).save(name, content, save=True)
        # add on post_save auto compress content field
        self.compress_file(async=True, delete_old_file=FILE_COMPRESS_DELETE_OLD_FILE)
