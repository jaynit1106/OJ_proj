from django.contrib import admin
from .models import Problem

class AdminProblem(admin.ModelAdmin):
    list_display=['question_name']

admin.site.register(Problem,AdminProblem)