from django.shortcuts import render,HttpResponse
from . import middleware


@middleware.verification
def index(request):
    if request.isverified:
        if request.log == 'f': 
            mynavbar = {
                'fname' : request.session.get('name'),
                'o1' : 'Profile',
                'o1l' : '/',
                'o2' : 'Logout',
                'o2l' : '/faculty/logout',
                'o3' : 'Student List',
                'o3l' : '/'

        }
            return render(request,'index.html',{'mynavbar':mynavbar})
        elif request.log == 'h':
            pass
        elif request.log == 's':
            pass
        else:
            mynavbar = {
                'fname' : 'User',
                 'o1' :'Faculties',
                 'o1l' : '/',
                  'o2' :'Faculty login',
                  'o2l' : '/faculty/login',
                   'o3' : 'Student login',
                   'o3l' : '/student/login'

        }
        return render(request,'index.html',{'mynavbar': mynavbar})

    else:
        mynavbar = {
                'fname' : 'User',
                 'o1' :'Faculties',
                 'o1l' : '/',
                  'o2' :'Faculty login',
                  'o2l' : '/faculty/login',
                   'o3' : 'Student login',
                   'o3l' : '/student/login'

        }
        return render(request,'index.html',{'mynavbar': mynavbar})
