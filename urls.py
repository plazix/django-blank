# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^account/', include('registration.backends.default.urls')),
)