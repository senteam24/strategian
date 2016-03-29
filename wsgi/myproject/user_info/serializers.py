from user_info.models import EventModel
from rest_framework import serializers
from user_info.models import UserModel
from user_info.models import ScheduleModel

class user_serializer(serializers.ModelSerializer):

    class Meta:
        model=UserModel
        fields=('name','program','email','student_id','password')

class user_reg_serializer(serializers.Serializer):
    success=serializers.IntegerField()
    user_info=serializers.JSONField()



class user_error_serializer(serializers.Serializer):
    success=serializers.IntegerField()
    message=serializers.CharField(max_length=500)


class event_serializer(serializers.ModelSerializer):
    class Meta:
        model=EventModel
        fields=('e_title','e_desc','e_date','e_time','e_end_date','e_end_time')

class schedule_serializer(serializers.ModelSerializer):

    class Meta:
        model=ScheduleModel
        fields=('user_id','title','desc','sch_date','sch_time','reminder_date','reminder_time')

class user_error:

    def __init__(self,success,message):
        self.success=success
        self.message=message

class user_reg:

    def __init__(self,success,user_info):
        self.success=success
        self.user_info=user_info