# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-31 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0012_auto_20170831_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
