# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-30 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_person_hash_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthdate',
            field=models.DateField(default='2000-05-12'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='profile_pic',
            field=models.FileField(blank=True, upload_to=login.models.profile_pic),
        ),
        migrations.AlterField(
            model_name='person',
            name='user_type',
            field=models.CharField(choices=[('TU', 'Tutor'), ('ST', 'Student'), ('AD', 'Admin')], default='ST', max_length=2),
        ),
    ]