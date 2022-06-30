import django
from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('',views.register_page,name='register_page')
]