from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Students, Course
from django.contrib import messages
import datetime
# Create your views here.

def home(request):
    obj = Course.objects.all()
    return render(request, 'home.html', {'obj': obj})


def addcourses(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name == "":
            error = "Something is wrong"
            return render(request, 'error.html', {'error': error})

        if len(Course.objects.filter(name=name)) != 0:
            error = "Already created Course"
            return render(request, 'error.html', {'error': error})        
        addrc = Course(name=name)
        addrc.save()
        messages.success(request, 'Course Sucessfully Added')
        return redirect('home')
    return render(request, 'addcourse.html')



def addstudents(request):
    obj = Course.objects.all()
    if request.method == 'POST':
        course = request.POST.get('course')
        name = request.POST.get('name')
        father = request.POST.get('father')
        dateofbirth = request.POST.get('dateofbirth')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        number = request.POST.get('number')
        email = request.POST.get('email')
        marks = request.POST.get('marks')
        if email == "":
            error = "Something is wrong"
            return render(request, 'error.html', {'error': error})

        if len(Students.objects.filter(email=email, number=number)) != 0:
            error = "Already created Student"
            return render(request, 'error.html', {'error': error}) 
        data = Students(course=course, name = name, father = father, dateofbirth = dateofbirth,address = address, city = city, state = state, pin = pin, number = number, email = email, marks = marks)        
        data.save()
        messages.success(request, 'Student Sucessfully Added')
        return redirect('home')        
                
    return render(request, 'addstudents.html',{'obj':obj})

def studentcourse(request, course_id):
    course = Course.objects.get(id=course_id)
    student = Students.objects.filter(course=course)
    return render(request, 'studentcourse.html',{'student':student})

def Studentsdetail(request, id):
    student =Students.objects.get(id=id)
    students = Students.objects.all()
    return render(request, 'studentsdetail.html',{'students':students, 'student':student})