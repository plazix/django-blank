# -*- coding: utf-8 -*-

import os, sys


########################################################################################################################
# Paths
########################################################################################################################


PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'vendors'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, MEDIA_URL.strip('/'))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip('/'))

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


########################################################################################################################
# Consts
########################################################################################################################


ADMINS = (
    ('Your Name', 'Your Email'),
)

MANAGERS = ADMINS

SITE_ID = 1

SECRET_KEY = 'your_secret_key'

'''
KEY_PATH = os.path.join(PROJECT_ROOT, 'var', 'data', 'secret.key')
try:
    SECRET_KEY = open(KEY_PATH).read()
except IOError:
    import random
    SECRET_KEY = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])
    open(KEY_PATH, 'w').write(SECRET_KEY)
'''


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
    'django.core.context_processors.static',
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

    #'core.middleware.git_revision.GitRevisionMiddleware',
    #'pagination.middleware.PaginationMiddleware',
)

# приложения
INSTALLED_APPS = (
    # apps
    'core',

    # 3rd party apps
    'south',
    #'pagination',
    #'annoying',
    'registration',
    #'sorl.thumbnail',

    # django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
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


########################################################################################################################
# Auth and register
########################################################################################################################


LOGIN_URL = '/account/login/'

LOGOUT_URL = '/account/logout/'

LOGIN_REDIRECT_URL = '/'

PASSWORD_RESET_TIMEOUT_DAYS = 3

ACCOUNT_ACTIVATION_DAYS = 3
