from django import forms
from django.forms.widgets import Select
from django.utils.regex_helper import Choice
from . import models

CHOICES = ['himansuh']
class TeacherForm(forms.ModelForm):
    # department = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model =  models.Teacher
        fields = '__all__'
        exclude = ['isverified']
        labels = {
            'fname' : 'First Name',
            'lname' : 'Last Name',
            'email' : 'Email ',
            'essn' :'Essn Number'
            ,'password' : 'Create Password'
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

                'department' : forms.Select(
               attrs ={ 'class':'form-control myselect' ,}
            ),
       
           
        }



class AssignmentForm(forms.ModelForm):
    # department = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model =  models.Assignment
        fields = '__all__'
        exclude = ['subject']
        labels = {
            'assignNumber' : 'Assignment Number',
            'section' : 'Section',
            'sem' : 'Semester',
            'assignment' :'Assignment'
            ,'dueDate' : 'Due Date'
      
            
        }
        widgets = {
            'assignNumber' : forms.Select(
               attrs ={ 'class' : 'form-control',}
            ),
                'section' : forms.Select(
               attrs ={ 'class' : 'form-control',}
            ),
                'sem' : forms.Select(
               attrs ={ 'class' : 'form-control',}
            ),
                'assignment' : forms.FileInput(
               attrs ={ 'class' : 'form-control', 'accept':"application/pdf"}
            ),
             
             
                'dueDate' : forms.DateInput(
               attrs ={ 'class' : 'form-control',}
            ),
             
             
               
       
           
        }