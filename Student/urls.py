from django.contrib import admin
from django.urls import path,include
from . import views as sv


urlpatterns = [
  
    path('registrations/',sv.index.as_view(),name='sshome' ),
    path('logout/',sv.StudentLogout.as_view(),name='logout' ),
    path('login/',sv.studentLogin.as_view(),name='login' ),
    path('profile/',sv.StudentProfile.as_view(),name='sprofile' ),
    path('checkAssign/st/<int:sem>/<str:sec>/<str:id>/<str:sub>/<int:tid>/',sv.CheckAssignment.as_view(),name='sassign' ),
    path('submit/assign/<int:id>/',sv.submitAssignment,name='sassign' ),
   
]
