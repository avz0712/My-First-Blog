# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

__author__ = 'Anrew Zaharovskyi'

urlpatterns = patterns('',
                       url(r'^about/$', 'Blog.views.about', name='about'),
                       url(r'^articles/(?P<article_id>\d+)/$', 'Blog.views.show_article', name='article'),
                       url(r'^articles/add_like/(?P<article_id>\d+)/$', 'Blog.views.add_like', name='like'),
                       url(r'^articles/add_comment/(?P<article_id>\d+)/$', 'Blog.views.add_comment', name='comment'),
                       url(r'^page/(\d+)/$', 'Blog.views.home', name='page'),
                       url(r'^$', 'Blog.views.home', name='home')
                       )
