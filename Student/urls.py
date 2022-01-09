from django.contrib import admin
from django.urls import path,include
from . import views as sv


urlpatterns = [
  
    path('registrations/',sv.index.as_view(),name='sshome' ),
   
]
