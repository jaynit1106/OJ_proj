from django.contrib import admin
from .models import Testcase

class AdminTestcase(admin.ModelAdmin):
    list_display=['question_name']

admin.site.register(Testcase,AdminTestcase)