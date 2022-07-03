from statistics import mode
from django.db import models
# Create your models here.
from problems.models import Problem
class Testcase(models.Model):
    question_name=models.ForeignKey(Problem,on_delete=models.CASCADE)
    input_tc=models.FileField(upload_to="input/",max_length=250,null=False,default=None)
    output_tc=models.FileField(upload_to="output/",max_length=250,null=False,default=None)