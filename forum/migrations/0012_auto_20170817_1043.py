# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-17 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_person_active_courses'),
        ('forum', '0011_auto_20170816_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='name',
        ),
        migrations.AddField(
            model_name='reply',
            name='author',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='login.Person'),
            preserve_default=False,
        ),
    ]
