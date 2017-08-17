# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-14 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20170720_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='slug',
            field=models.CharField(default='value', max_length=36),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='thread',
            name='slug',
            field=models.CharField(default='value', max_length=36),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reply',
            name='replied_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Thread'),
        ),
    ]
