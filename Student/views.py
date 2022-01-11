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

                if len(Student.objects.filter(usn = usn.upper())) !=0:
                    messages.info(request,'USN Exist Already')
                    return render(request,'Student/index.html',{'sform' : sform})

                Student.objects.create(department= models.HOD.objects.get(department=department),fname=fname,lname=lname,email=email,password=password,sem = sem,simg=request.FILES['simg'],usn=usn.upper(),cycle=cycle,mobile=mobile,section = section
                ).save()
                request.session['name'] = fname
                request.session['essn'] = str(usn)
                request.session['log'] = 's'
            return HttpResponseRedirect('/')



    


class StudentLogout(View):
    @method_decorator(verification) 
    def get(self, request):
         if request.isverified:
            if request.log == 'f' or request.session['log'] == 'h' or request.log == 's':
                del request.session['log']
                del request.session['name']
                del request.session['essn']
                return HttpResponseRedirect('/')
         else:
             return HttpResponse('<h1> Bad request</h1>')



class studentLogin(View):
    @method_decorator(verification)
    def get(self, request):
         if request.isverified:
                return HttpResponse('<h1> bad request </h1>')
         else:
            mynavbar = {
                'fname' : 'User',
                 'o1' :'New Faculty',
                 'o1l' : '/faculty/new/teacher/registration',
                  'o2' :'Faculty login',
                  'o2l' : '/faculty/login',
                   'o3' : 'Student login',
                   'o3l' : '/student/login'

        }
            return render(request,'Student/slogin.html',{'mynavbar': mynavbar})
    @method_decorator(verification)
    def post(self, request):
         if request.isverified:
                return HttpResponse('<h1> bad request </h1>')
         else:
            usn = request.POST.get('usn')
            password = request.POST.get('password')

            if usn == "":
                messages.info(request,'Please enter the usn')
                return HttpResponseRedirect('/student/login')
            elif password == "":
                messages.info(request,'Please enter the password')
                return HttpResponseRedirect('/student/login')
            else:
                checkDATA = Student.objects.filter(usn =usn.upper())

                if len(checkDATA) == 0:
                    messages.info(request,'incorrect Details')
                    return HttpResponseRedirect('/student/login')
                elif len(checkDATA) > 1:
                    messages.info(request,'incorrect Details Error mv 1')
                    return HttpResponseRedirect('/student/login')
                else:
                        for i in checkDATA:
                            passw = i.password
                            fname = i.fname
                        
                        if passw == password :
                        
                            request.session['name'] = fname
                            request.session['essn'] = str(usn)
                            request.session['log'] = 's'
            
                            return HttpResponseRedirect('/')
                        else:
                            messages.info(request,'incorrect Details')
                            return HttpResponseRedirect('/student/login')




         
         


class StudentProfile(View):
    @method_decorator(verification)
    def get(self, request):
        if request.isverified:
            if request.log == 's':
                st = Student.objects.filter(usn = request.session.get('essn').upper())
                if len(st) == 0:
                    return HttpResponse(" <h1> Bad request error not Exist </h1>")
                elif len(st) > 1:
                     return HttpResponse(" <h1> Bad request error not Exist error code mv s1 </h1>")
                else:
                    mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Works',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/student/logout',
                'o3' : 'Student List',
                'o3l' : '/'

                }
           
                return render(request, 'Student/sprofile.html',{'mynavbar': mynavbar ,'st':st})
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/student/login')