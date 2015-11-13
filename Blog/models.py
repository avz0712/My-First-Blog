# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime

__author__ = 'Anrew Zaharovskyi'


# Create your models here.
SHORT_TEXT_LEN = 350


class Article(models.Model):
    class Meta():
        db_table = 'article'

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_user = models.ForeignKey(User)
    article_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    article_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.article_title

    def get_short_text(self):
        if len(self.article_text) > SHORT_TEXT_LEN:
            return self.article_text[:SHORT_TEXT_LEN]
        else:
            return self.article_text


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    # comments_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    comments_text = models.TextField(verbose_name='Text for comment:')
    comments_article = models.ForeignKey(Article)
    comments_from = models.ForeignKey(User)
