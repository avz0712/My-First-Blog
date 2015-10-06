# -*- coding: utf-8 -*-
from django.contrib import admin
from Blog.models import Article, Comments


# Register your models here.


class ArticleInLine(admin.StackedInline):
    model = Comments
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    fields = [
        'article_title',
        'article_text',
        'article_user',
        'article_date'
    ]

    inlines = [ArticleInLine]

    list_filter = ['article_title',
                   'article_date'
                   ]


admin.site.register(Article, ArticleAdmin)
