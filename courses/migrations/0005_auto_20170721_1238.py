# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-21 12:38
from __future__ import unicode_literals

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_course_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='guide',
            field=models.FileField(upload_to=courses.models.guide_location),
        ),
    ]
