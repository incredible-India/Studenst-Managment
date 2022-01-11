from django.shortcuts import render,HttpResponse
from . import middleware


@middleware.verification
def index(request):
    if request.isverified:
        if request.log == 'f': 
            mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Profile',
                'o1l' : '/faculty/teacher/profile/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'

        }
            return render(request,'index.html',{'mynavbar':mynavbar})
        elif request.log == 'h':
            mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Profile',
                'o1l' : '/faculty/hod/profile/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'

        }
            return render(request,'index.html',{'mynavbar':mynavbar})
           
        elif request.log == 's':
            mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Profile',
                'o1l' : '/student/profile/',
                'o2' : 'Logout',
                'o2l' : '/student/logout',
                'o3' : 'Student List',
                'o3l' : '/'

        }
            return render(request,'index.html',{'mynavbar':mynavbar})
          
        else:
            mynavbar = {
                'fname' : 'User',
                 'o1' :' New Faculty',
                 'o1l' : '/faculty/new/teacher/registration',
                  'o2' :'Faculty login',
                  'o2l' : '/faculty/login',
                   'o3' : 'Student login',
                   'o3l' : '/student/login'

        }
        return render(request,'index.html',{'mynavbar': mynavbar})

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
        return render(request,'index.html',{'mynavbar': mynavbar})
