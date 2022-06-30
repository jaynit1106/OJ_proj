from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register_page(request):
    return render(request,'register.html')

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
                return redirect('http://localhost:8000/home/')
        else:
            messages.info(request,'Passwords not matching')
            return render(request,'register.html')
    else:
        return HttpResponse('Something is wrong')
