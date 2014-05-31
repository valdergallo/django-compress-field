# -*- coding: utf-8 -*-
import os
from django.test import TestCase
from example.core.models import MyContent
from django.core.files.base import File
from django.conf import settings

BASEDIR = os.path.dirname(__file__)
FIXTURE = os.path.join(BASEDIR, 'data', 'text.txt')


class TestCompressTestCase(TestCase):

    def setUp(self):
        self.dummyfile = File(open(FIXTURE, 'r'), name='test_fixture.txt')
        try:
            temp_file_path = os.path.join(settings.MEDIA_ROOT, 'mycontent', 'test_fixture.txt')
            os.unlink(temp_file_path)
        except (IOError, OSError, AttributeError):
            pass

    def create_my_content(self):
        my_content = MyContent()
        my_content.name = 'test'
        my_content.upload_file = self.dummyfile
        my_content.save()
        return my_content

    def test_save_file_on_model(self):
        my_content = self.create_my_content()

        self.assertEqual(my_content.upload_file.name, 'mycontent/test_fixture.txt')

    def test_save_zipfile_on_model(self):
        my_content = self.create_my_content()
        my_content.upload_file.compress()

        self.assertEqual(my_content.upload_file.name, 'mycontent/test_fixture.zip')

    def test_is_compress_has_updated_register(self):
        my_content = self.create_my_content()
        my_content.upload_file.compress()

        my_content = MyContent.objects.get(id=my_content.id)
        self.assertEqual(my_content.upload_file.name, 'mycontent/test_fixture.zip')

    def test_if_is_compressed_must_return_true(self):
        my_content = self.create_my_content()
        my_content.upload_file.compress()
        self.assertTrue(my_content.upload_file.is_compressed)

    def test_if_is_compressed_must_return_false(self):
        my_content = self.create_my_content()
        self.assertFalse(my_content.upload_file.is_compressed)

    def test_compress_name(self):
        my_content = self.create_my_content()
        self.assertEqual(my_content.upload_file.compress_name, 'mycontent/test_fixture.zip')
