# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-06 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import forum.models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0016_reply_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploaded',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=forum.models.upload_file)),
            ],
        ),
        migrations.RemoveField(
            model_name='reply',
            name='file',
        ),
        migrations.RemoveField(
            model_name='thread',
            name='file',
        ),
        migrations.AddField(
            model_name='fileuploaded',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='forum.Reply'),
        ),
        migrations.AddField(
            model_name='fileuploaded',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread', to='forum.Thread'),
        ),
    ]
