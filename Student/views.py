from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views import View
from .forms import StudentForm
from django.contrib import messages
from .validation import checkStudentFrom
from .models import Student
from Faculty import models
# Create your views here.
from django.utils.decorators import method_decorator
from Student_Management.middleware import verification 
class index(View):
    @method_decorator(verification)
    def get(self, request):
        if request.isverified:
            return HttpResponseRedirect('/')
        
        elif request.session.get('log',None) == 'h' or request.session.get('log',None) == 'f' or request.session.get('log',None) == 's':
            return HttpResponseRedirect('/')

        
        else:

            sform = StudentForm()
            mynavbar = {
                'fname' : 'User',
                 'o1' :'New Faculty',
                 'o1l' : '/faculty/new/teacher/registration',
                  'o2' :'Faculty login',
                  'o2l' : '/faculty/login',
                   'o3' : 'Student login',
                   'o3l' : '/student/login'

        }
            return render(request, 'Student/index.html',{'sform': sform,'mynavbar': mynavbar})

    @method_decorator(verification)   
    def post(self, request):
        if request.isverified:
            return HttpResponseRedirect('/')
        
        elif request.session.get('log',None) == 'h' or request.session.get('log',None) == 'f' or request.session.get('log',None) == 's':
            return HttpResponseRedirect('/')
        
        else:
            sform = StudentForm(request.POST)
            if sform.is_valid():
                check = checkStudentFrom(sform.cleaned_data)
            else:
                check = checkStudentFrom(sform.cleaned_data)

            
            if check[0] == 0:
                 messages.info(request,check[1])
                 return render(request,'Student/index.html',{'sform' : sform})

            else:
                fname = check[1]['fname']
                lname = check[1]['lname']
                email = check[1]['email']
                password = check[1]['password']
                sem = check[1]['sem']
                section = check[1]['section']
                mobile = check[1]['mobile']
                usn = check[1]['usn']
                department = request.POST.get('department')
                cycle = check[1]['cycle']
        
                Student.objects.create(department= models.HOD.objects.get(department=department),fname=fname,lname=lname,email=email,password=password,sem = sem,simg=request.FILES['simg'],usn=usn.upper(),cycle=cycle,mobile=mobile,section = section
                ).save()
                request.session['name'] = fname
                request.session['essn'] = str(usn)
                request.session['log'] = 's'
            return HttpResponseRedirect('/')



    