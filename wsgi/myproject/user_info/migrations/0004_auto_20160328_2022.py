# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0003_eventmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='student_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
