
from django.conf.urls import url
from user_info import views
urlpatterns = [
    url(r'^user_reg',views.user_view.as_view()),
    url(r'^login',views.login_view.as_view()),
    url(r'^get_event',views.event_view.as_view()),
    url(r'^schedule',views.schedule_view.as_view()),
]

