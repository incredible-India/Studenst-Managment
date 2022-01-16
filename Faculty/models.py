from django.db import models
from django.db.models.base import Model
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
Sec_CHOICES =(
    ("1", "A"),
    ("2", "B"),
    ("3", "C"),
    ("4", "D"),

)

Sem_CHOICES =(
    ("1", "1st sem"),
    ("2", "2nd sem"),
    ("3", "3rd sem"),
    ("4", "4th sem"),
    ("5", "5th sem"),
    ("6", "6th sem"),
    ("7", "7th sem"),
    ("8", "8th sem"),

)



# Create your models here.
# base class 
class Faculty(models.Model):
    fname = models.CharField(max_length=50,null=False)
    lname = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=50,null=False)
    essn = models.CharField(max_length=50,null=False,unique=True)
    password = models.CharField(max_length=50,null=False)
    fimg = models.ImageField(upload_to='./static/Faculty/img')
    degree = models.TextField()
    class Meta:
        abstract = True



class HOD(Faculty):
    
    department = models.CharField(max_length=50,null=False)
    isteacher = models.BooleanField(default=False)


class Teacher(Faculty):
    department = models.ForeignKey(HOD,on_delete=models.CASCADE, default='')
    isverified = models.BooleanField(default=False)


    


class Teaches(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    section = models.CharField(max_length=10,choices = Sec_CHOICES,default=None)
    sem = models.CharField(max_length=10,null=False,choices = Sem_CHOICES,default=None)
    subject = models.CharField(max_length=40,null=False)



class ClassTeacher(models.Model):
    # teachers = Teacher.objects.all()

    # if len(teachers) ==0:
    #     teacherdata = [('None','No teacher Available')]
    # else:
    #     teacherdata = []
    #     for i in teachers:
    #         teacherdata.append((i.id,i.fname)) 

    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    section = models.CharField(max_length=10,default=None)
    sem = models.CharField(max_length=10,null=False,default=None)


class Assignment(models.Model):
    subject = models.ForeignKey(Teaches, on_delete=models.CASCADE)
    assignNumber = models.IntegerField()
    dueDate = models.DateField()





