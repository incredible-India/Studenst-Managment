from django.db import models
from Faculty.models import HOD,Teacher
# Create your models here.

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
class Student(models.Model):
    department = models.ForeignKey(HOD,on_delete=models.CASCADE)
    classTeacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,default=None)
    fname = models.CharField(max_length=50,null=False)
    lname = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=50,null=False,default=None)
    usn = models.CharField(max_length=15 ,null=False,unique=True)
    email = models.EmailField(max_length=50)
    mobile =models.BigIntegerField()
    sem = models.CharField(max_length=10,null=False,choices = Sem_CHOICES,default=None)
    section = models.CharField(max_length=3 ,choices = Sec_CHOICES,default=None,null=False)
    cycle = models.CharField(max_length=20,default=None)
    simg  = models.ImageField(upload_to='./static/student/img', default=None)
    isverified = models.BooleanField(default=False)
