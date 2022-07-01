from unicodedata import name
import django
from django.urls import path
from . import views

urlpatterns=[
    path('create',views.register,name='register'),
    path('register',views.register_page,name='register_page'),
    path('login',views.login_page,name='login_page'),
    path('auth',views.login,name='auth'),
    path('logout',views.logout,name='logout'),

]