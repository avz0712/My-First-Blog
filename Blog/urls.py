# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'Blog.views.home', name='home'),
                       url(r'^about$', 'Blog.views.about', name='about'),
                       url(r"^articles/(?P<article_id>\d+)/$", 'Blog.views.show_article', name='article')
                       )
