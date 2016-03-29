from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=200)
    student_id=models.IntegerField(primary_key=True)
    program=models.CharField(max_length=10)
    password=models.CharField(max_length=100)

class ScheduleModel(models.Model):
    user_id=models.ForeignKey(UserModel)
    title=models.CharField(max_length=100)
    desc=models.TextField()
    sch_date=models.DateField()
    sch_time=models.TimeField()
    reminder_time=models.TimeField()
    reminder_date=models.DateField()

class EventModel(models.Model):
    e_title=models.CharField(max_length=120)
    e_desc=models.TextField()
    e_date=models.DateField()
    e_time=models.TimeField()
    e_end_date=models.DateField()
    e_end_time=models.TimeField()