# -*- coding: utf-8 -*-
try:
    from celery.task import task
except ImportError:
    task = None


@task(serializer='pickle')
def task_compress_wrapper(instance, field, delete_old_file):
    instance_field = getattr(instance, field)
    instance_field.compress(async=False, delete_old_file=delete_old_file)
    return True
