from django.contrib import admin
from .models import Submission

class AdminSubmission(admin.ModelAdmin):
    list_display=['username','question_name','status']

admin.site.register(Submission,AdminSubmission)