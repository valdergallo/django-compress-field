# -*- coding: utf-8 -*-
import os
import unittest
from example.core.models import MyContent

BASEDIR = os.path.dirname(__file__)
FIXTURE = os.path.join(BASEDIR, 'fixtures', 'text.txt')


class TestCompressField(unittest.TestCase):

    def setUp(self):
        self.dummyfile = open(FIXTURE, 'r')

    def test_save_file_on_model(self):
        my_content = MyContent()
        my_content.name = 'test'
        my_content.upload_file = self.dummyfile
        my_content.save()

        self.assertEqual(my_content.id, 1)
