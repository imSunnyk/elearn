# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-07 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20170907_1011'),
        ('series', '0004_auto_20170907_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesreply',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.Person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seriesthread',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.Person'),
            preserve_default=False,
        ),
    ]
