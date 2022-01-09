from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    # department = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model =  Student
        fields = ['fname','lname','usn','email','mobile','section','sem','cycle','department','classTeacher','simg','password']
        exclude = ['isverified']
        labels = {
            'fname' : 'First Name',
            'lname' : 'Last Name',
            'email' : 'Email ',
            'usn' :'Usn Number'
            ,'password' : 'Create Password'
            ,'simg'  : 'Profile Image'
            ,'sem' : 'Semester'
            ,'section' : 'Section'
            ,'classTeacher' : 'Class Teacher'
            ,
            'department' : 'Branch',
            'mobile' : 'Mobile',
            'cycle' : 'Cycle',
           
            
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
                'usn' : forms.TextInput(
               attrs ={ 'class' : 'form-control',}
            ),
                'password' : forms.PasswordInput(
               attrs ={ 'class' : 'form-control',}
            ),
                'simg' : forms.FileInput(
               attrs ={ 'class' : 'form-control',}
            ),
               'section' : forms.Select(attrs = { 
                    'class':'form-control  mb-3 address' ,'rows':'2','placeholder' : 'B.Tech,M.Tech'
                }),

                'sem' : forms.Select(attrs = { 
                    'class':'form-control  mb-3 address' ,'rows':'2','placeholder' : 'B.Tech,M.Tech'
                }),

                'department' : forms.Select(
               attrs ={ 'class':'form-control myselect' ,}
            ),
                'classTeacher' : forms.Select(
               attrs ={ 'class':'form-control myselect' ,}
            ),

             'mobile' : forms.NumberInput(attrs = { 
                    'class':'form-control  mb-3 address' 
                }),

                      'cycle' : forms.Select(
               attrs ={ 'class' : 'form-control',}
            ),



       
           
        }


