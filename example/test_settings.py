import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BASEDIR = os.path.dirname(__file__)

ADMINS = (
    ('My Exampel', 'example@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '::memory::',
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(BASEDIR, 'media')
STATIC_ROOT = os.path.join(BASEDIR, 'static')

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/admin/media/'

SECRET_KEY = '*)7&l7ri*t%kat%+sfujmtc9sw*o&114mx56&2nt&-l0xad*_w'

TEMPLATE_LOADERS = (
)

MIDDLEWARE_CLASSES = (
)

ROOT_URLCONF = 'example.urls'

TEMPLATE_DIRS = (
    os.path.join(BASEDIR, 'template'),
)

INSTALLED_APPS = (
    # 'django.contrib.auth',
    #'django.contrib.contenttypes',
    #'django.contrib.sessions',
    # 'django.contrib.sites',
    # 'django.contrib.messages',
    # 'django.contrib.admin',
    # 'django.contrib.admindocs',
    'example.core',
    'compress_field',
)
