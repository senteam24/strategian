# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0005_auto_20160328_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='student_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
