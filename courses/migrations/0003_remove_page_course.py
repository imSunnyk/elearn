# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-20 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='course',
        ),
    ]
