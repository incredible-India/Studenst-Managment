import re
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
from Student.models import Student 
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
                StudentAproval = Student.objects.filter(Q(isverified =False) & Q(department = hoddepart.id))

           

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
           
                return render(request, 'Faculty/hodView.html',{'mynavbar': mynavbar ,'hoddata':hoddata,'teacherAproval' :len(teaherAproval),'studentAproval':len(StudentAproval)})
                

                    
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



        


# single Aproval Faculty 

class ApprovalInduvidual(View):
    
    def get(self, request,id):
        fname = request.session.get('name',None)
        essn = request.session.get('essn',None)
        log = request.session.get('log',None)

        if fname == None and essn == None and log == None:
            return HttpResponseRedirect('/faculty/login')
        else:
            if log == 'h':

                # checking the hod verification
                hod = models.HOD.objects.filter(essn = essn)
                if len(hod) == 0:
                    return HttpResponse("<h1> Unauthorised Access </h1>")
                else:
                    hods = models.HOD.objects.get(essn = essn)
                    teacher = models.Teacher.objects.get(essn = id)

                    if hods.department == teacher.department.department:
                        updateinfo = models.Teacher.objects.filter(essn = id).update(isverified = True)
                        return HttpResponseRedirect('/faculty/hod/teacher/aproval/')
                    else:
                             return HttpResponse("<h1> Unauthorised Access </h1>")



                
          
            else:
                return HttpResponse(" <h1> Bad request </h1>")



class ApprovalForAllFaculty(View):
    @method_decorator(middleware.verification)
    def get(self, request):
         if request.isverified:
            if request.session['log'] == 'h':
          
                hod = models.HOD.objects.filter(Q(essn = request.essn) & Q(fname = request.fname))

                if len(hod) == 0:
                    return HttpResponse("<h1> Unauthorised Access </h1>")
                else:
                    hods = models.HOD.objects.get(essn = request.essn)

                    teacher = models.Teacher.objects.all()

                    for i in teacher :
                        if i.department.department == hods.department:
                            models.Teacher.objects.filter(id=i.id).update(isverified = True)

                    
                    return HttpResponseRedirect("/faculty/hod/teacher/aproval/")



# Approva for the student individial

class giveStudentApproval(View):
    @method_decorator(middleware.verification)
    def get(self, request):
        if request.isverified:
            if request.log =='h':
                hoddepart = models.HOD.objects.get(essn =  request.session['essn'])
             
                StudentAproval = Student.objects.filter(Q(isverified =False) & Q(department = hoddepart.id))
                mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'
                }
           
                return render(request, 'Student/aproveStudent.html',{'mynavbar': mynavbar ,'teacherAproval' :len(StudentAproval),'toaprove' : StudentAproval})
                
            else:
                return HttpResponse('<h1> Bad Request </h1>')
        else:
            return HttpResponseRedirect('/faculty/login')



class StudentAprovalIndividual(View):
    def get(self, request,id):
        fname = request.session.get('name',None)
        essn = request.session.get('essn',None)
        log = request.session.get('log',None)

        if fname == None and essn == None and log == None:
            return HttpResponseRedirect('/faculty/login')
        else:
            if log == 'h':

                # checking the hod verification
                hod = models.HOD.objects.filter(essn = essn)
                if len(hod) == 0:
                    return HttpResponse("<h1> Unauthorised Access </h1>")
                else:
                    hods = models.HOD.objects.get(essn = essn)
                    students = Student.objects.get(usn = id.upper())

                    if hods.department == students.department.department:
                        updateinfo = Student.objects.filter(usn = id.upper()).update(isverified = True)
                        return HttpResponseRedirect('/faculty/hod/student/aproval/')
                    else:
                             return HttpResponse("<h1> Unauthorised Access </h1>")



                
          
            else:
                return HttpResponse(" <h1> Bad request </h1>")
       


class studentAllApproval(View):

    @method_decorator(middleware.verification)
    def get(self, request):
         if request.isverified:
            if request.session['log'] == 'h':
          
                hod = models.HOD.objects.filter(Q(essn = request.essn) & Q(fname = request.fname))

                if len(hod) == 0:
                    return HttpResponse("<h1> Unauthorised Access </h1>")
                else:
                    hods = models.HOD.objects.get(essn = request.essn)

                    students = Student.objects.all()

                    for i in students :
                        if i.department.department == hods.department:
                            Student.objects.filter(id=i.id).update(isverified = True)

                    
                    return HttpResponseRedirect("/faculty/hod/student/aproval/")




# Genral Profile for all
@middleware.verification
def checkUserLogin(request):
    if request.isverified:
       

        return [True,request.log]
    else:
        return [False]

class Genralprofile(View):
    def get(self, request,whome,id):
        
        k = checkUserLogin(request)

        if k[0] == True:
            if request.log == 'h':
                mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'
                }
            elif request.log == 'f':
                mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'
                }
            elif request.log == 's':
                mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'
                }
            else:
                mynavbar = {
                'fname' : 'User',
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'
                }
        else:
            mynavbar = {
                'fname' : 'User',
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'
                }

        mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'
                }
        
        if whome == 'teacher':
            teacherdata =  models.Teacher.objects.filter(essn = id)
            if len(teacherdata) == 0:
                return HttpResponse('<h1>Bad Request</h1>')
            else:
                return render(request, 'Faculty/GeneralProfile.html',{'mynavbar' : mynavbar,'data' : 1,'teacherdata':teacherdata})
        elif whome == 'hod':
            HODdata =  models.HOD.objects.filter(essn = id)
            if len(HODdata) == 0:
                return HttpResponse('<h1>Bad Request</h1>')
            else:
                return render(request, 'Faculty/GeneralProfile.html',{'mynavbar' : mynavbar,'data' : 2,'HODdata':HODdata})
       
        elif whome == 'student':
            St =  Student.objects.filter(usn = id.upper())
            if len(St) == 0:
                return HttpResponse('<h1>Bad Request</h1>')
            else:
                return render(request, 'Faculty/GeneralProfile.html',{'mynavbar' : mynavbar,'data':3,'St':St})
        
        else:
            return HttpResponse('<h1> Bad request </h1>') 
    




# Assign class teacher
class classTeacher(View):
    @method_decorator(middleware.verification)
    def get(self, request):
        if  request.isverified:
            if request.log == 'h':
                classteacher =  models.ClassTeacher.objects.all()

                Hod = models.HOD.objects.get(essn = request.essn)
                teachers = models.Teacher.objects.filter(department = Hod.id)

         

                if len(teachers) == 0:
                    t = 0
                else:
                    t = teachers
                if len(classteacher) == 0:
                    ct = 0
                else:
                    ct = classteacher
                
                mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'
                }

                return render(request,'Faculty/classteacher.html',{'mynavbar': mynavbar ,'t':t,'ct':ct})

                


            else:
                return HttpResponse('<h1> You Have Not Permission For This </h1>')
        else:
                return HttpResponseRedirect('/faculty/login')
    
    @method_decorator(middleware.verification)
    def post(self, request):
        if  request.isverified:
            if request.log == 'h':
                sec  = request.POST.get('sec')
                sem  = request.POST.get('sem')
                ct  = request.POST.get('ct')
                
                info = models.ClassTeacher.objects.filter(Q(sem = sem) & Q(section= sec))
                # models.ClassTeacher.objects.update_or_create(section = sec ,sem = sem,teacher = models.Teacher.objects.get(id = ct))
                if len(info) != 1:
                    models.ClassTeacher.objects.create(sem = sem,section = sec,teacher = models.Teacher.objects.get(id = ct)).save()
                else:
                    info.update(teacher = models.Teacher.objects.get(id = ct))
                return HttpResponseRedirect('/faculty/assign/classteacher')
            else:
                return HttpResponse('<h1> You Have Not Permission For This </h1>')
        else:
            return HttpResponseRedirect('/faculty/login')




# for the list of student hod view
class studentList(View):
    @method_decorator(middleware.verification)
    def get(self, request):

        if  request.isverified:
 
            st = Student.objects.all()
            mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'
                }
            return render(request,'Faculty/stlist.html',{'mynavbar':mynavbar,'st':st,'all':1})

            
        else:
         
            return HttpResponseRedirect('/faculty/login')

class teacherList(View):
    @method_decorator(middleware.verification)
    def get(self, request):

        if  request.isverified:
 
            st = models.Teacher.objects.all()
            mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'
                }
            return render(request,'Faculty/teaclist.html',{'mynavbar':mynavbar,'st':st,'all':1})

            
        else:
         
            return HttpResponseRedirect('/faculty/login')
        
        