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
    path('teacher/profile/',views.teacherProfile.as_view(),name='tprofile'),
    path('hod/profile/',views.HodProfile.as_view(),name='hprofile'),
    path('hod/teacher/aproval/',views.giveAproval.as_view(),name='happroval'),
    path('teacher/<str:id>/aproveit/',views.ApprovalInduvidual.as_view()),
    path('teacher/approve/all/faculties/',views.ApprovalForAllFaculty.as_view(),name='happrovalall'),
    path('hod/student/aproval/',views.giveStudentApproval.as_view(),name='studentapprove'),
    path('student/<str:id>/aproveit/',views.StudentAprovalIndividual.as_view(),name='studentapprove'),
    path('student/approve/student/',views.studentAllApproval.as_view(),name='stapprovalall'),
    path('<str:whome>/<str:id>/',views.Genralprofile.as_view(),name='stapprovalall'),
    path('assign/classteacher',views.classTeacher.as_view(),name='classteacher'),
    path('student/list/',views.stlist.as_view(),name='classteacher'),
]
