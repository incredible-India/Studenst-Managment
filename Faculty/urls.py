from django.contrib import admin
from django.urls import path,include
from . import views as sameView
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('new/teacher/registration/',views.NewTeacher.as_view(),name='teacherform'),
    path('logout/',views.facultyLogout.as_view(),name='logout'),
    path('login/',views.facultyLogin.as_view(),name='logout'),

]