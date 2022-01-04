from django.db import models
from django.db.models.base import Model

# Create your models here.
# base class 
class Faculty(models.Model):
    fname = models.CharField(max_length=50,null=False)
    lname = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=50,null=False)
    essn = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=50,null=False)
    fimg = models.ImageField(upload_to='./static/img/')
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
    section = models.CharField(max_length=10)
    sem = models.CharField(max_length=10,null=False)
    subject = models.CharField(max_length=40,null=False)


class Assignment(models.Model):
    subject = models.ForeignKey(Teaches, on_delete=models.CASCADE)
    assignNumber = models.IntegerField()
    dueDate = models.DateField()