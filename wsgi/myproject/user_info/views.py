
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from user_info.models import UserModel
from user_info.serializers import user_serializer
from user_info.serializers import user_error_serializer
from user_info.validate import check_student_id_exists
from user_info.serializers import user_error
from user_info.serializers import user_reg_serializer
from user_info.serializers import user_reg
from user_info.validate import check_login_exists
from user_info.models import EventModel
from user_info.serializers import event_serializer
from user_info.models import ScheduleModel
from user_info.serializers import schedule_serializer
from rest_framework import viewsets
# Create your views here.s


class user_view(APIView):

    def post(self,request):
        name=request.POST.get("name","")
        student_id=request.POST.get("student_id","")
        program=request.POST.get("program","")
        email=request.POST.get("email","")
        password=request.POST.get("password","")
        print "name="+name
        if(name!="" and  student_id!="" and program!="" and email!="" and password!=""):
            if check_student_id_exists(student_id,email)==0:
                value=UserModel(name=name,student_id=student_id,program=program,email=email,password=password)
                value.save()
                reg_obj=user_reg(success=1,user_info=user_serializer(value).data)
                return Response(user_reg_serializer(reg_obj).data)

            else :
                success=-1
                message="User Already Exists"

                return Response(user_error_serializer(user_error(success=success,message=message)).data)

        else:
                success=-2
                message="Syntax Error. "
                return Response(user_error_serializer(user_error(success=success,message=message)).data)




class login_view(APIView):

    def post(self,request):
        student_id=request.POST.get("student_id","")
        password=request.POST.get("password","")
        print student_id
        print password
        if(student_id!="" and password!=""):
            log_val=check_login_exists(student_id,password)
            if(isinstance(log_val,UserModel)):
                log_obj=(user_reg(success=1,user_info=user_serializer(log_val).data))
                return Response(user_reg_serializer(log_obj).data)
            else:
                success=-1;
                message="Login Credential not authentic.Register!"
                return Response(user_error_serializer(user_error(success=success,message=message)).data)

        else:
                success=-1;
                message="Syntax Error"
                return Response(user_error_serializer(user_error(success=success,message=message)).data)




class event_view(APIView):

    def get(self,request):
        query_set=EventModel.objects.all()
        event=event_serializer(query_set,many=True)
        return Response(event.data)

class schedule_view(APIView):

    def get(self,request):
        user_id=request.GET.get("user_id","")
        queryset=ScheduleModel.objects.get(user_id=user_id)
        serializer_class=schedule_serializer(queryset,many=True)
        return Response(serializer_class.data)

    def post(self,request):
        serializer=schedule_serializer(data=request.data)
        if(serializer.is_valid()==True):
            serializer.save()
            return Response(1)
        else:
            return Response(-1)