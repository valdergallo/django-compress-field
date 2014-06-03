# -*- coding: utf-8 -*-
import os
import shutil
from django.test import TestCase
from example.core.models import MyContent
from django.core.files.base import File
from django.conf import settings
try:
    ioError = WindowsError
except NameError:
    ioError = IOError

BASEDIR = os.path.dirname(__file__)
FIXTURE = os.path.join(BASEDIR, 'data', 'text.txt')

UPLOADED_FILE_FULL_PATH = os.path.join(settings.MEDIA_ROOT, 'mycontent/2014/06/03/', 'test_fixture.txt')
UPLOADED_ZIPFILE_FULL_PATH = os.path.join(settings.MEDIA_ROOT, 'mycontent/2014/06/03/', 'test_fixture.zip')

UPLOADED_FILE_PATH = os.path.join('mycontent/2014/06/03/', 'test_fixture.txt')
UPLOADED_ZIPFILE_PATH = os.path.join('mycontent/2014/06/03/', 'test_fixture.zip')
UPLOADED_ZIPFILE2_PATH = os.path.join('mycontent/2014/06/03/', 'test_fixture_1.zip')


class TestCompressTestCase(TestCase):

    def setUp(self):
        self.dummyfile = File(open(FIXTURE, 'r'), name='test_fixture.txt')

    def tearDown(self):
        shutil.rmtree(os.path.join(settings.MEDIA_ROOT, 'mycontent'), ignore_errors=True)

    def create_my_content(self):
        my_content = MyContent()
        my_content.name = 'test'
        my_content.upload_file = self.dummyfile
        my_content.save()
        return my_content

    def test_save_file_on_model(self):
        my_content = self.create_my_content()
        self.assertEqual(my_content.upload_file.name, UPLOADED_FILE_PATH)

    def test_save_zipfile_on_model(self):
        my_content = self.create_my_content()
        my_content.upload_file.compress()

        self.assertEqual(my_content.upload_file.name, UPLOADED_ZIPFILE_PATH)

    def test_is_compress_has_updated_register(self):
        my_content = self.create_my_content()
        my_content.upload_file.compress()

        my_content = MyContent.objects.get(id=my_content.id)
        self.assertEqual(my_content.upload_file.name, UPLOADED_ZIPFILE_PATH)

    def test_if_is_compressed_must_return_true(self):
        my_content = self.create_my_content()
        my_content.upload_file.compress()
        self.assertTrue(my_content.upload_file.is_compressed)

    def test_if_is_compressed_must_return_false(self):
        my_content = self.create_my_content()
        self.assertFalse(my_content.upload_file.is_compressed)

    def test_compress_name(self):
        my_content = self.create_my_content()
        self.assertEqual(my_content.upload_file.compress_name, UPLOADED_ZIPFILE_PATH)

    def test_if_compress_delete_file_uncompress(self):
        my_content = self.create_my_content()
        my_content.upload_file.compress()

        self.assertFalse(os.path.exists(UPLOADED_FILE_PATH))

    def test_if_zip_is_not_override_names(self):
        my_content = self.create_my_content()
        my_content.upload_file.compress()
        self.assertEqual(my_content.upload_file.name, UPLOADED_ZIPFILE_PATH)

        my_content2 = self.create_my_content()
        my_content2.upload_file.compress()
        self.assertEqual(my_content2.upload_file.name.replace('\\', '/'), UPLOADED_ZIPFILE2_PATH)
