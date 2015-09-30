# -*- coding: utf-8 -*-
try:
    from celery.task import task
except ImportError:
    task = None

from django.core.cache import cache
from django.conf import settings
LOCK_EXPIRE = 60 * 5

FILE_COMPRESS_QUEUE = getattr(settings, 'FILE_COMPRESS_QUEUE', 'Celery')


# cache.add fails if if the key already exists
def acquire_lock(lock_id):
    return cache.add(lock_id, 'true', LOCK_EXPIRE)


# memcache delete is very slow, but we have to use it to take
# advantage of using add() for atomic locking
def release_lock(lock_id):
    return cache.delete(lock_id)


@task(serializer='pickle', queue=FILE_COMPRESS_QUEUE)
def task_compress_wrapper(instance, field, delete_old_file):
    lock_id = '{0}-io-lock-{1}'.format(instance.__class__.__name__, instance.id)

    if acquire_lock(lock_id):
        instance_field = getattr(instance, field)
        instance_field.compress(async=False, delete_old_file=delete_old_file)
        release_lock(lock_id)
        return True

    # task is locked by IO
    print('IO Lock Task')
    return False
