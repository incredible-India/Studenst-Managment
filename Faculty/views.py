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
from django.db.models import Q 
# Create your views here.

class NewTeacher(View):
    @method_decorator(middleware.verification) 
    def get(self,request):
        if request.isverified:
          return HttpResponseRedirect('/')
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
            if request.log == 'f' or request.session['log'] == 'h':
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
                 'o1' :'New Faculty',
                 'o1l' : '/faculty/new/teacher/registration',
                  'o2' :'Faculty login',
                  'o2l' : '/faculty/login',
                   'o3' : 'Student login',
                   'o3l' : '/student/login'

        }
            return render(request,'Faculty/login.html',{'mynavbar': mynavbar})
    @method_decorator(middleware.verification)   
    def post(self, request):
        if request.isverified:
            if request.session['log'] == 'f' or request.session['log'] == 'h':
                return HttpResponseRedirect('/')
        
        else:
            essn = request.POST.get('essn')
            password = request.POST.get('password')
            ishod = request.POST.get('ishod') 
            # for the hod
            if ishod != None:
                    checkHODValidation = validation.checkvalidationHOD(essn,password)
                    if checkHODValidation[0] == 0:
                        messages.info(request,checkHODValidation[1])
                        return HttpResponseRedirect('/faculty/login')
                    
                    else:
            
                        for i in checkHODValidation[1]:
                            fname = i.fname
                        request.session['name'] = fname
                        request.session['essn'] = str(essn)
                        request.session['log'] = 'h'
                        
                        return HttpResponseRedirect('/')

            # for the Faculty
            else:

                checkValidation = validation.validatilogin(essn,password,ishod) 

                if checkValidation[0] == 0:
                 messages.info(request,checkValidation[1])
                 return HttpResponseRedirect('/faculty/login')
   
                
                else:
                    for i in checkValidation[1]:
                        fname = i.fname
                    request.session['name'] = fname
                    request.session['essn'] = str(essn)
                    request.session['log'] = 'f'
                    mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'others',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'

        }           
                return HttpResponseRedirect('/')
                    # return render(request, 'Faculty/teacherView.html',{'mynavbar': mynavbar})
    


class teacherProfile(View):
    @method_decorator(middleware.verification)
    def get(self, request):
        if request.isverified:
            if request.session['log'] == 'f':
                teacherdata = models.Teacher.objects.filter(essn =  request.session['essn'])
                if len(teacherdata) == 0:
                    return HttpResponse(" <h1> Bad request error not Exist </h1>")
                else:
                    mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'

                }
           
                return render(request, 'Faculty/teacherView.html',{'mynavbar': mynavbar ,'teacherdata':teacherdata})
                

                    
            else:
                return HttpResponse(" <h1> Bad request </h1>")
        else:
            return HttpResponseRedirect('/faculty/login/')



# for the prifile of hod

class HodProfile(View):
    @method_decorator(middleware.verification)
    def get(self, request):
        if request.isverified:
            if request.session['log'] == 'h':
                hoddata = models.HOD.objects.filter(essn =  request.session['essn'])
                hoddepart = models.HOD.objects.get(essn =  request.session['essn'])
             
                teaherAproval = models.Teacher.objects.filter(Q(isverified =False) & Q(department = hoddepart.id))

           

                if len(hoddata) == 0:
                    return HttpResponse(" <h1> Bad request error not Exist </h1>")
                else:
                    mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'

                }
           
                return render(request, 'Faculty/hodView.html',{'mynavbar': mynavbar ,'hoddata':hoddata,'teacherAproval' :len(teaherAproval)})
                

                    
            else:
                return HttpResponse(" <h1> Bad request </h1>")
        else:
            return HttpResponseRedirect('/faculty/login/')



# for thr aproval list  
class giveAproval(View):
    @method_decorator(middleware.verification)
    def get(self, request):
        if request.isverified:
            if request.session['log'] == 'h':
                hoddepart = models.HOD.objects.get(essn =  request.session['essn'])
             
                teaherAproval = models.Teacher.objects.filter(Q(isverified =False) & Q(department = hoddepart.id))
                mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'
                }
           
                return render(request, 'Faculty/aproveteacher.html',{'mynavbar': mynavbar ,'teacherAproval' :len(teaherAproval),'toaprove' : teaherAproval})
            else:
                return HttpResponse(" <h1> Bad request </h1>")
        else:
            return HttpResponseRedirect('/faculty/login/')  