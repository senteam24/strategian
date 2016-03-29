# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('reminder_time', models.TimeField()),
                ('reminder_date', models.DateField()),
                ('flag', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.UserModel')),
            ],
        ),
    ]
