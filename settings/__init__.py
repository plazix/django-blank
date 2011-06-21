# -*- coding: utf-8 -*-

try:
    from development import *
except ImportError:
    try:
        from production import *
    except ImportError:
        assert False, u'Missing config files'