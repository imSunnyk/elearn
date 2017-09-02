# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-31 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0009_auto_20170831_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='course',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='group',
            name='tutors',
            field=models.ManyToManyField(blank=True, related_name='tutors', to='login.Tutor'),
        ),
        migrations.AlterField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='users', to='login.Person'),
        ),
    ]