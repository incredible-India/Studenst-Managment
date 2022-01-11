from django.contrib import admin
from django.urls import path,include
from . import views as sv


urlpatterns = [
  
    path('registrations/',sv.index.as_view(),name='sshome' ),
    path('logout/',sv.StudentLogout.as_view(),name='logout' ),
    path('login/',sv.studentLogin.as_view(),name='login' ),
    path('profile/',sv.StudentProfile.as_view(),name='sprofile' ),
   
]
