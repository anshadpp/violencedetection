import datetime
from django.db import models

# Create your models here.


class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Department(models.Model):
    departmentname=models.CharField(max_length=100)

class Course(models.Model):
    coursename=models.CharField(max_length=100)
    DEPARTMENT=models.ForeignKey(Department,on_delete=models.CASCADE)

class Staff(models.Model):
    name=models.CharField(max_length=100)
    dateofbirth=models.DateField()
    gender=models.CharField(max_length=100)
    DEPARTMENT=models.ForeignKey(Department,on_delete=models.CASCADE)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    dist=models.CharField(max_length=100)
    pin=models.IntegerField()
    photo = models.CharField(max_length=300, default=0)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Student(models.Model):
    name=models.CharField(max_length=100)
    dateofbirth=models.DateField()
    gender=models.CharField(max_length=100)
    COURSE=models.ForeignKey(Course,on_delete=models.CASCADE)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    place=models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin=models.IntegerField()
    dist=models.CharField(max_length=100)
    guardianname=models.CharField(max_length=100)
    guardianemail=models.CharField(max_length=100)
    guardianphone=models.BigIntegerField()
    photo=models.CharField(max_length=300,default=0)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)

class Authority(models.Model):
    name=models.CharField(max_length=100)
    dateofbirth=models.DateField()
    gender=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    LOGIN=models.ForeignKey(Login, on_delete=models.CASCADE)

# class Attendance(models.Model):
#     STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)
#     time=models.CharField(max_length=100)
#     date=models.DateField()
#     photo=models.CharField(max_length=100)
#     status=models.CharField(max_length=100)



class Attendance(models.Model):
    date=models.DateField()
    time=models.CharField(max_length=15, default=datetime.datetime.now().strftime('%H:%M'))
    hour=models.CharField(max_length=100)
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)


class Complaint(models.Model):
    date=models.DateField()
    LOGIN=models.ForeignKey(Login, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)

class Chat(models.Model):
    FROM=models.ForeignKey(Login,on_delete=models.CASCADE, related_name='from_id')
    TO=models.ForeignKey(Login,on_delete=models.CASCADE, related_name='to_id')
    message=models.CharField(max_length=100)
    date=models.DateField()

class Latenotification(models.Model):
    date=models.DateField()
    time=models.CharField(max_length=100)
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)

class Violence(models.Model):
    time=models.CharField(max_length=100)
    date=models.DateField()
    photo=models.CharField(max_length=100)

class Violenceincludedface(models.Model):
    STUDENT=models.ForeignKey(Student, on_delete=models.CASCADE)
    VIOLENCE=models.ForeignKey(Violence,on_delete=models.CASCADE)
