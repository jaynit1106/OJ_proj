import imp
from django.shortcuts import render
from django.http import HttpResponse

import problems
from .models import Problem

def all_question(request):
    problems=Problem.objects.all()
    return render(request,'home.html',{'problems':problems})

def get_question(request,question_id):
    try:
        problem=Problem.objects.get(pk=question_id)
        print(problem.question_desc)
        return render(request,'problems.html',{'problem':problem})
    except:
        return HttpResponse("Problem Does not Exist")