# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-14 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0006_auto_20170811_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='slug',
            field=models.CharField(max_length=36),
        ),
    ]
