from django.db import models
from django.contrib.humanize.templatetags import humanize



class Course(models.Model):
    name = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)

    def get_date(self):
        return humanize.naturaltime(self.create_at)
    def __str__(self):
        return self.name


class Students(models.Model):
    course = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    father= models.CharField(max_length=250)
    dateofbirth = models.DateField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=45)
    pin = models.CharField(max_length=6)
    number = models.CharField(max_length=13, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    marks = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_date(self):
        return humanize.naturaltime(self.create_at)
    def __str__(self):
        return self.name

    
