from django.http import response
from django.shortcuts import redirect, render,HttpResponse,HttpResponseRedirect
# from cryptography.fernet import Ferne 
from django.views import View
from . import models 
from . import forms
from .  import validation
from django.contrib import messages
from django.utils.decorators import method_decorator
from Student_Management import middleware
# Create your views here.

class NewTeacher(View):
    def get(self,request):
        teacherForm = forms.TeacherForm()
       
        return render(request,'faculty/newTeacher.html',{'form' : teacherForm})
    
    def post(self,request):
        teacherDATA = forms.TeacherForm(request.POST)
        if  teacherDATA.is_valid():
            checkData = validation.validateTeacherForm(teacherDATA.cleaned_data)
        else:
            checkData = validation.validateTeacherForm(teacherDATA.cleaned_data)
      
        if checkData[0] == 0:
            
            messages.info(request,checkData[1])
            return render(request,'faculty/newTeacher.html',{'form' : teacherDATA})
        else:
            checkExistance = models.Teacher.objects.filter(essn = teacherDATA.cleaned_data['essn'])
            if len(checkExistance) !=0:
                messages.info(request,'Essn Already Exists')
                return render(request,'faculty/newTeacher.html',{'form' : teacherDATA})
            else:
                fname = teacherDATA.cleaned_data['fname']
                lname = teacherDATA.cleaned_data['lname']
                email = teacherDATA.cleaned_data['email']
                password = teacherDATA.cleaned_data['password']
                essn = teacherDATA.cleaned_data['essn']
           
                degree = teacherDATA.cleaned_data['degree']
                department = request.POST.get('department')
                print(degree, department)
                models.Teacher.objects.create(department=models.HOD.objects.get(department=department),fname=fname,lname=lname,email=email,password=password,degree=degree,fimg=request.FILES['fimg'],essn=essn
                ).save()
                request.session['name'] = fname
                request.session['essn'] = str(essn)
                request.session['log'] = 'f'
            return HttpResponseRedirect('/')
 

class facultyLogout(View):
    @method_decorator(middleware.verification)
    def get(self, request):
        if request.isverified:
            if request.log == 'f':
                del request.session['log']
                del request.session['name']
                del request.session['essn']
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('<h1> Bad Request </h1>')
        else :
            return HttpResponse('<h1> Bad Request </h1>')

class facultyLogin(View):
    @method_decorator(middleware.verification)
    def get(self, request):
        if request.isverified:
            return HttpResponse('<h1> Bad Request </h1>')
        else :
            mynavbar = {
                'fname' : 'User',
                 'o1' :'Faculties',
                 'o1l' : '/',
                  'o2' :'Faculty login',
                  'o2l' : '/faculty/login',
                   'o3' : 'Student login',
                   'o3l' : '/student/login'

        }
            return render(request,'Faculty/login.html',{'mynavbar': mynavbar})
        
    def post(self, request):
        pass
