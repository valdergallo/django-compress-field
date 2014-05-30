# -*- coding: utf-8 -*-
try:
    from celery.task import task
except ImportError:
    task = None

import zipfile
import os

from django.conf import settings
from django.db.models import FileField
from django.core.files.storage import Storage
FILE_COMPRESS_DELETE_OLD_FILE = getattr(settings, 'FILE_COMPRESS_DELETE_OLD_FILE', True)


class CompressStorage(Storage):
    compress_ext = 'zip'

    def _save(self, name, content):
        return super(CompressStorage, self)._save(name, content)


class FileCompressorField(FileField):
    compress_ext = 'zip'

    def is_compressed(self, file_name):
        basename, ext = os.path.splitext(file_name)
        return self.compress_ext == ext

    @property
    def filefield_instance(self):
        return getattr(self.model_instance, self.get_attname())

    def get_compress_name(self):
        basename, ext = os.path.splitext(self.filefield_instance.name)
        return basename + ('.' + self.compress_ext)

    def compress_content(self, delete_old_file=True):
        """
        Method to change for new implementations
        """
        compress_file_fullname = self.get_compress_name()

        if self.is_compressed(compress_file_fullname):
            return

        in_memory_zip = file(compress_file_fullname, 'w')
        ziped = zipfile.ZipFile(in_memory_zip, "w", zipfile.ZIP_DEFLATED)
        ziped.write(self.filefield_instance.name)
        ziped.close()

        self.save_compress_content(ziped, delete_old_file)
        return ziped

    # def save_compress_content(self, file_content, delete_old_file=True):
    #     file = super(FileField, self).pre_save(self.model_instance, True)
    #     setattr(file, '_committed', True)
    #     #if delete_old_file:  # remove old file
    #         # os.unlink(self.filefield_instance.name)
    #         # self.storage.delete(self.name)

    #     compress_name = self.get_compress_name()
    #     # save zipfile on database
    #     if file and not file._committed:
    #         return file.save(compress_name, file_content, save=False)
    #     return file

    def compress_file(self, model_instance=None, async=True, delete_old_file=True):
        if async and task:
            file_content = task(self.compress_content).delay(delete_old_file=delete_old_file)
        else:
            file_content = self.compress_content(delete_old_file=delete_old_file)

        return file_content

    # def pre_save(self, model_instance, add):
    #     # add on post_save auto compress content field
    #     self.model_instance = model_instance
    #     self.compress_file(async=True, delete_old_file=FILE_COMPRESS_DELETE_OLD_FILE)
