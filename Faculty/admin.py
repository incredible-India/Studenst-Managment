from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.HOD)
class HODAdmin(admin.ModelAdmin):
    list_display = ['id','fname','lname','email','essn','password', 
    'fimg','degree','department','isteacher']


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','fname','lname','email','essn','password', 
    'fimg','degree','isverified','department']


@admin.register(models.Teaches)
class TeachesAdmin(admin.ModelAdmin):
    list_display = ['id','section','teacher','sem','subject']


@admin.register(models.Assignment)
class TeachesAdmin(admin.ModelAdmin):
    list_display = ['id','subject','assignNumber','sem','section','assignment','dueDate']


@admin.register(models.ClassTeacher)
class  ClassTeacherAdmin(admin.ModelAdmin):
    list_display = ['section','teacher','sem']