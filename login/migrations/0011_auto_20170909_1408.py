# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-09 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20170909_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='person_series_id',
            new_name='person_series',
        ),
    ]