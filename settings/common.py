# -*- coding: utf-8 -*-

import os, sys


########################################################################################################################
# Consts
########################################################################################################################


ADMINS = (
    ('Your Name', 'Your Email'),
)

MANAGERS = ADMINS

SITE_ID = 1

SECRET_KEY = 'your secret key'


########################################################################################################################
# Default settings
########################################################################################################################


ROOT_URLCONF = 'urls'

DEFAULT_FROM_EMAIL = 'no-reply@yourdomain.tld'

DEFAULT_FILE_STORAGE = 'core.storage.TransliteratedStorage'


########################################################################################################################
# Locale, encoding, time
########################################################################################################################


TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru'

DEFAULT_CHARSET = 'UTF-8'


########################################################################################################################
# Paths
########################################################################################################################


PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'vendors'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, MEDIA_URL.strip('/'))

STORAGE_URL = MEDIA_URL + 'storage/'
STORAGE_ROOT = os.path.join(PROJECT_ROOT, STORAGE_URL.strip('/'))

ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'


########################################################################################################################
# Templates
########################################################################################################################


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
)


########################################################################################################################
# Apps
########################################################################################################################


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    #'pagination.middleware.PaginationMiddleware',
)

# приложения
INSTALLED_APPS = (
    # apps
    'core',

    # 3rd party apps
    #'grappelli.dashboard',
    #'grappelli',
    #'pagination',
    #'annoying',
    #'registration',
    #'sorl.thumbnail',

    # django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
)


########################################################################################################################
# Logging
########################################################################################################################


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] %(asctime)s - %(message)s',
            'datefmt': '%d.%m.%Y %H:%M:%S',
        },
    },
    'handlers': {

    },
    'loggers': {

    },
}


