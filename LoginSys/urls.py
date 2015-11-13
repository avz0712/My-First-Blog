# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

__author__ = 'Anrew Zaharovskyi'

urlpatterns = patterns('',
                       url(r'^login/$', 'LoginSys.views.login'),
                       url(r'^logout/$', 'LoginSys.views.logout'),
                       url(r'^register/$', 'LoginSys.views.register')
                       )
