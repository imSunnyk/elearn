# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-16 11:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_thread_forum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='forum',
        ),
    ]
