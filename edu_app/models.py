from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=90)
    number = models.CharField(max_length=10)
    message = models.TextField(max_length=120)

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=90)
    course = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    message = models.TextField(max_length=120)

    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=90)
    event = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    message = models.TextField(max_length=120)

    def __str__(self):
        return self.name      


class Student(models.Model):
    choose = [ ('A+','A +ve'), ('B+','B +ve'),('AB+','AB +ve'),
    ('O+','O +ve'),('O-','O -ve'),('AB-','AB-ve')]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=13)
    blood_group = models.CharField(max_length=4,choices=choose, null=True)
    parents_name = models.CharField(max_length=50)
    address = models.CharField(max_length=70, default='')
    prof = models.ImageField(upload_to='edu_app/images', default='')
    def __str__(self):
        return self.user.username

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=13)
    designation = models.CharField(max_length=50)
    address = models.CharField(max_length=70, default='')
    prof = models.ImageField(upload_to='edu_app/images', default='')
    def __str__(self):
        return self.user.username

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=250)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=250)
    file = models.FileField(upload_to='edu_app/assignments')
    deadline = models.DateTimeField()
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

