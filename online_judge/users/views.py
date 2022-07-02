from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register_page(request):
    return render(request,'register.html')

def login_page(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        username=request.POST['first_name']
        password=request.POST['password']
        password1=request.POST['password1']
        email=request.POST['email']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken')
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name)
                user.save()
                return redirect('http://localhost:8000/users/login')
        else:
            messages.info(request,'Passwords not matching')
            return render(request,'register.html')
    else:
        return HttpResponse('Something is wrong')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('http://localhost:8000/problems/')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,'login.html')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('http://localhost:8000/users/login')