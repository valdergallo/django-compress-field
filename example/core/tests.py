# -*- coding: utf-8 -*-
import os
from django.test import TestCase
from example.core.models import MyContent
from django.core.files.base import File

BASEDIR = os.path.dirname(__file__)
FIXTURE = os.path.join(BASEDIR, 'fixtures', 'text.txt')


class TestCompressTestCase(TestCase):

    def setUp(self):
        self.dummyfile = File(FIXTURE)

    def test_save_file_on_model(self):
        my_content = MyContent()
        my_content.name = 'test'
        my_content.upload_file = self.dummyfile
        my_content.save()

        self.assertEqual(my_content.upload_file, 'text.txt')
