# -*- coding: utf-8 -*-

import os
import sys

sys.path = [os.path.dirname(__file__)] + sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()