from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['fname','lname','usn','email','section','sem','cycle','mobile','id','department','simg','password','isverified','classTeacher']
# Register your models here.
