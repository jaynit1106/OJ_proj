from . import views
from django.urls import path
urlpatterns=[
    path('<username>/<question_name>/submit',views.submit,name="submit"),
    path('<username>/submissions',views.view_submissions,name='view_submissions'),
]