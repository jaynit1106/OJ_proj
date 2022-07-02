from email.policy import default
from random import choices
from secrets import choice
from django.db import models
from django.forms import CharField

# Create your models here.
class Problem(models.Model):
    difficulty_choices=(
        ('hard','HARD'),
        ('medium','MEDIUM'),
        ('easy','EASY'),
    )
    status_choices=(
        ('solved','SOLVED'),
        ('unsolved','UNSOLVED'),
    )
    question_name=models.CharField(max_length=20)
    question_desc=models.TextField(max_length=250)
    difficulty=models.CharField(max_length=6,choices=difficulty_choices,default='easy')
    time_limit=models.IntegerField(default=1000,help_text='in milliseconds')
    input_format=models.TextField(max_length=50)
    output_format=models.TextField(max_length=50)
    status=models.CharField(max_length=8,choices=status_choices,default='unsolved')