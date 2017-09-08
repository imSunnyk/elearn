# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-08 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20170831_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_slug', models.CharField(max_length=36)),
            ],
        ),
        migrations.CreateModel(
            name='Subchapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subch_name', models.CharField(max_length=100)),
                ('subch_slug', models.CharField(max_length=36)),
                ('subch_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subch_book', to='courses.Book')),
            ],
        ),
        migrations.RenameField(
            model_name='course',
            old_name='code',
            new_name='course_code',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='desc',
            new_name='course_desc',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='guide',
            new_name='course_guide',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='slug',
            new_name='course_slug',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='desc',
            new_name='page_desc',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='slug',
            new_name='page_slug',
        ),
        migrations.RenameField(
            model_name='week',
            old_name='course',
            new_name='week_course',
        ),
        migrations.RenameField(
            model_name='week',
            old_name='name',
            new_name='week_name',
        ),
        migrations.RenameField(
            model_name='week',
            old_name='slug',
            new_name='week_slug',
        ),
        migrations.RemoveField(
            model_name='page',
            name='name',
        ),
        migrations.RemoveField(
            model_name='page',
            name='week',
        ),
        migrations.AddField(
            model_name='page',
            name='page_name',
            field=models.CharField(default='Null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='book_week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_week', to='courses.Week'),
        ),
        migrations.AddField(
            model_name='page',
            name='page_book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_book', to='courses.Book'),
        ),
        migrations.AddField(
            model_name='page',
            name='page_subch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='page_subch', to='courses.Subchapter'),
        ),
    ]
