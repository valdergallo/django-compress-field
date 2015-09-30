# -*- coding: utf-8 -*-
try:
    from celery.task import task
except ImportError:
    task = None

import os
from django.conf import settings
from django.db.models.fields.files import FieldFile

FILE_COMPRESS_DELETE_OLD_FILE = getattr(settings, 'FILE_COMPRESS_DELETE_OLD_FILE', True)


class CompressFieldFile(FieldFile):
    compress_ext = None

    def _is_compressed(self):
        basename, ext = os.path.splitext(self.name)
        compress_ext = '.' + self.compress_ext
        return compress_ext == ext
    is_compressed = property(_is_compressed)

    def _base_name(self):
        return os.path.basename(self.file.name)
    base_name = property(_base_name)

    def _compress_name(self):
        if not hasattr(self, '_avaliable_compress_name'):
            basename, ext = os.path.splitext(self.name)
            compress_name = basename + ('.' + self.compress_ext)
            self._avaliable_compress_name = self.storage.get_available_name(compress_name)
        return self._avaliable_compress_name

    compress_name = property(_compress_name)

    def _compress_full_name(self):
        return os.path.join(self.storage.location, self.compress_name)

    compress_full_name = property(_compress_full_name)

    def get_available_name(self):
        return self.storage.get_available_name(self.compress_name)

    def compress_content(self):
        """
        Method to change for new implementations
        """
        raise NotImplementedError()

    def _update_filefield_name(self, delete_old_file=True):
        # update field value
        old_name = self.name

        setattr(self.instance, self.field.name, self.compress_name)
        self.instance.save()

        if delete_old_file:
            self.file.close()
            self.storage.delete(old_name)

    def compress_wrapper(self, delete_old_file):
        self.compress_content()
        self._update_filefield_name(delete_old_file=delete_old_file)
        return True

    def compress(self, async=True, delete_old_file=FILE_COMPRESS_DELETE_OLD_FILE):
        if self.is_compressed:
            return u'This file is alredy compress'

        if async and task:
            from .tasks import task_compress_wrapper
            wrapper = task_compress_wrapper.delay(self.instance, self.field.name, delete_old_file)
        else:
            wrapper = CompressFieldFile.compress_wrapper(self, delete_old_file)

        return wrapper
