from django.contrib import admin
from django.urls import path,include
from . import views as sameView
from . import views 

urlpatterns = [

    path('new/teacher/registration/',views.NewTeacher.as_view(),name='teacherform'),

]
