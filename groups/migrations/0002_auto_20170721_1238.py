# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-21 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='tutors',
            field=models.ManyToManyField(related_name='tutors', to='login.Tutor'),
        ),
    ]
