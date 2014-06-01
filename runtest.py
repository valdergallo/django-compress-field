#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'example.test_settings'
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)

def runtests():
    from django.test.utils import get_runner
    from django.conf import settings

    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=2, interactive=True)
    failures = test_runner.run_tests(['core'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    runtests()
