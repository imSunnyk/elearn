# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-19 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0002_auto_20170819_1059'),
        ('groups', '0007_auto_20170721_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='series', to='series.Series'),
            preserve_default=False,
        ),
    ]
