# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-06 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0017_auto_20170906_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileuploaded',
            name='slug',
            field=models.CharField(default='aaaaaa', max_length=36),
            preserve_default=False,
        ),
    ]
