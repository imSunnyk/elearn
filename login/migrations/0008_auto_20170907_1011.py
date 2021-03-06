# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-07 10:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0004_auto_20170907_1011'),
        ('login', '0007_auto_20170830_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_series', to='series.Series'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
