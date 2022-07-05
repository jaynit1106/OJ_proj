from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from problems.models import Problem
import datetime
# Create your models here.

class Submission(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    question_name=models.ForeignKey(Problem,on_delete=models.CASCADE)
    language=models.CharField(max_length=20,default="c++")
    code=models.TextField()
    status=models.CharField(max_length=10)
    date=models.DateTimeField(default=datetime.datetime.now())
    