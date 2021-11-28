from django.urls import path, re_path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('addcourses', views.addcourses, name='addcourses'),
    path('addstudents', views.addstudents, name='addstudents'),
    path('studentcourse/<int:course_id>/', views.studentcourse, name='studentcourse'),
    path('Studentsdetail/<int:id>/', views.Studentsdetail, name='Studentsdetail'),
    
]