from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.views import View
from .forms import StudentForm
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
    