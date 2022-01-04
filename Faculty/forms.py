from django import forms
from django.forms.widgets import Select
from . import models


class TeacherForm(forms.ModelForm):
    class Meta:
        model =  models.Teacher
        fields = '__all__'
        exclude = ['isverified']
        labels = {
            'fname' : 'First Name',
            'lname' : 'Last Name',
            'email' : 'Email ',
            'essn' :'Essn Number'
            ,'password' : 'Password'
            ,'fimg'  : 'Profile Image'
            ,'degree' : 'Degrees'
            ,
            'department' : 'Department'
            
        }
        widgets = {
            'fname' : forms.TextInput(
               attrs ={ 'class' : 'form-control',}
            ),
                'lname' : forms.TextInput(
               attrs ={ 'class' : 'form-control',}
            ),
                'email' : forms.EmailInput(
               attrs ={ 'class' : 'form-control',}
            ),
                'essn' : forms.TextInput(
               attrs ={ 'class' : 'form-control',}
            ),
                'password' : forms.PasswordInput(
               attrs ={ 'class' : 'form-control',}
            ),
                'fimg' : forms.FileInput(
               attrs ={ 'class' : 'form-control',}
            ),

                'degree' : forms.Textarea(attrs = { 
                    'class':'form-control  mb-3 address' ,'rows':'2','placeholder' : 'B.Tech,M.Tech'
                }),

                'department' : Select(
               attrs ={ 'class':'form-control' ,}
            ),
           
        }