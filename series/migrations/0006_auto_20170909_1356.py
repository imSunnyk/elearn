# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-09 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_auto_20170907_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='name',
            new_name='series_name',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='slug',
            new_name='series_slug',
        ),
        migrations.RenameField(
            model_name='seriesfileuploaded',
            old_name='file',
            new_name='series_file_file',
        ),
        migrations.RenameField(
            model_name='seriesfileuploaded',
            old_name='slug',
            new_name='series_file_slug',
        ),
        migrations.RenameField(
            model_name='seriesreply',
            old_name='adate',
            new_name='series_reply_adate',
        ),
        migrations.RenameField(
            model_name='seriesreply',
            old_name='author',
            new_name='series_reply_author',
        ),
        migrations.RenameField(
            model_name='seriesreply',
            old_name='desc',
            new_name='series_reply_desc',
        ),
        migrations.RenameField(
            model_name='seriesreply',
            old_name='replied_to',
            new_name='series_reply_replied_to',
        ),
        migrations.RenameField(
            model_name='seriesreply',
            old_name='slug',
            new_name='series_reply_slug',
        ),
        migrations.RenameField(
            model_name='seriesthread',
            old_name='adate',
            new_name='series_thread_adate',
        ),
        migrations.RenameField(
            model_name='seriesthread',
            old_name='author',
            new_name='series_thread_author',
        ),
        migrations.RenameField(
            model_name='seriesthread',
            old_name='desc',
            new_name='series_thread_desc',
        ),
        migrations.RenameField(
            model_name='seriesthread',
            old_name='name',
            new_name='series_thread_name',
        ),
        migrations.RenameField(
            model_name='seriesthread',
            old_name='series',
            new_name='series_thread_series',
        ),
        migrations.RenameField(
            model_name='seriesthread',
            old_name='slug',
            new_name='series_thread_slug',
        ),
        migrations.RemoveField(
            model_name='seriesfileuploaded',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='seriesfileuploaded',
            name='thread',
        ),
        migrations.AddField(
            model_name='seriesfileuploaded',
            name='series_file_reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='series_file_reply', to='series.SeriesReply'),
        ),
        migrations.AddField(
            model_name='seriesfileuploaded',
            name='series_file_thread',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='series_file_thread', to='series.SeriesThread'),
            preserve_default=False,
        ),
    ]