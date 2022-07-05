from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.all_question,name='all questions'),
    path('<question_id>/',views.get_question,name='get_question'),
    path('name/<question_name>/',views.get_question_byname,name="get_question_byname"),
]