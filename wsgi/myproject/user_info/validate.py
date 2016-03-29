from user_info.models import EventModel
from user_info.models import UserModel
from django.db.models import Q

def check_student_id_exists(student_id,email):
    user=UserModel.objects.filter(Q(student_id=student_id) | Q(email=email)).count()
    return user


def check_login_exists(student_id,password):
    user=UserModel.objects.filter(Q(student_id=student_id) & Q(password=password))

    if(len(user)==1):
        return user.first()
    elif(len(user)==0):
        return 0
    else:
        return -1

def check_event(date,time):
    events=UserModel.objects.filter(Q(EventModel.e_date>date) & Q(EventModel.e_time>time))

    if(len(events)>0):
        return  events
    elif(len(events)==0):
        return 0
    else:
        return -1