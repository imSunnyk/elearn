# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-21 12:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_auto_20170721_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='tutors',
        ),
    ]
