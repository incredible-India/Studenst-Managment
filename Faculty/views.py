from django.shortcuts import render
from django.views import View
from . import models 
from . import forms

# Create your views here.

class NewTeacher(View):
    def get(self,request):
        teacherForm = forms.TeacherForm()
        return render(request,'faculty/newTeacher.html',{'form' : teacherForm})
