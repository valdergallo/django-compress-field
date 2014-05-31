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
    compress_ext  = None

    def _is_compressed(self):
        basename, ext = os.path.splitext(self.name)
        return self.compress_ext == ext
    is_compressed = property(_is_compressed)

    def _compress_name(self):
        basename, ext = os.path.splitext(self.name)
        return basename + ('.' + self.compress_ext)
    compress_name = property(_compress_name)

    # In addition to the standard File API, FieldFiles have extra methods
    # to further manipulate the underlying file, as well as update the
    # associated model instance.
    def save(self, name, content, save=True):
        name = self.field.generate_filename(self.instance, name)
        self.name = self.storage.save(name, content)
        setattr(self.instance, self.field.name, self.name)

        # Update the filesize cache
        self._size = content.size
        self._committed = True

        # Save the object because it has changed, unless save is False
        if save:
            self.instance.save()
    save.alters_data = True

    def delete(self, save=True):
        # Only close the file if it's already open, which we know by the
        # presence of self._file
        if hasattr(self, '_file'):
            self.close()
            del self.file

        self.storage.delete(self.name)

        self.name = None
        setattr(self.instance, self.field.name, self.name)

        # Delete the filesize cache
        if hasattr(self, '_size'):
            del self._size
        self._committed = False

        if save:
            self.instance.save()
    delete.alters_data = True

    def get_compress_name(self):
        basename, ext = os.path.splitext(self.name)
        return basename + ('.' + self.compress_ext)

    def compress_content(self, delete_old_file=True):
        """
        Method to change for new implementations
        """
        raise NotImplementedError()

    def _update_filefield_name(self):
        # update field value
        setattr(self.instance, self.field.name, self.compress_name)
        self.instance.save()

    def compress(self, async=True, delete_old_file=True):
        if async and task:
            file_content = task(self.compress_content).delay(delete_old_file=delete_old_file)
        else:
            file_content = self.compress_content(delete_old_file=delete_old_file)

        self._update_filefield_name()

        return file_content
