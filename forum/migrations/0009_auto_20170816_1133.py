# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-16 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_thread_forum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='forum',
            field=models.ForeignKey(default='0000000', editable=False, on_delete=django.db.models.deletion.CASCADE, to='forum.Forum'),
        ),
    ]
