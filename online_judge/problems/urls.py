from django.urls import path
from . import views

urlpatterns=[
    path('',views.all_question,name='all questions'),
    path('<question_id>/',views.get_question,name='get_question')
]