# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20151113_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
    ]
