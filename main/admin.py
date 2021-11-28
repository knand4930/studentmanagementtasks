from django.contrib import admin
from .models import *
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at')
    list_fiter = ('name',)
    
admin.site.register(Course ,CourseAdmin)


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'course','father', 'email', 'number')
    list_fiter = ('course','create_at', 'email', 'number')
    
admin.site.register(Students ,StudentsAdmin)