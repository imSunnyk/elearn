# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-16 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_person_active_courses'),
        ('forum', '0010_auto_20170816_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('adate', models.DateField(auto_now=True)),
                ('slug', models.CharField(max_length=36)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Person')),
                ('forum', models.ForeignKey(default=111, editable=False, on_delete=django.db.models.deletion.CASCADE, to='forum.Forum')),
            ],
        ),
        migrations.AddField(
            model_name='reply',
            name='replied_to',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='forum.Thread'),
            preserve_default=False,
        ),
    ]
