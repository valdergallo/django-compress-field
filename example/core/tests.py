# -*- coding: utf-8 -*-
import os
from django.test import TestCase
from example.core.models import MyContent
from django.core.files.base import File
from django.conf import settings

BASEDIR = os.path.dirname(__file__)
FIXTURE = os.path.join(BASEDIR, 'fixtures', 'text.txt')


class TestCompressTestCase(TestCase):

    def setUp(self):
        self.dummyfile = File(open(FIXTURE, 'r'), name=FIXTURE)
        try:
            temp_file_path = os.path.join(settings.MEDIA_ROOT, 'mycontent', 'text.txt')
            os.unlink(temp_file_path)
        except (IOError, WindowsError, AttributeError):
            pass

    def test_save_file_on_model(self):
        my_content = MyContent()
        my_content.name = 'test'
        my_content.upload_file = self.dummyfile
        my_content.save()

        self.assertEqual(my_content.upload_file.name, 'mycontent/text.txt')
