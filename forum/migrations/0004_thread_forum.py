# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-16 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20170814_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='forum',
            field=models.ForeignKey(default = 11, on_delete=django.db.models.deletion.CASCADE, to='forum.Forum'),
            preserve_default=False,
        ),
    ]