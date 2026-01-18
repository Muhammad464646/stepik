from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(blank=True)
    avatar=models.ImageField(upload_to='avatars/',null=True,blank=True)


class Course(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)


class Module(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    description=models.TextField()
    is_active=models.BooleanField(default=True)


class Task(models.Model):
    module=models.ForeignKey(Module,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    order=models.IntegerField()
    description=models.TextField()


class Submission(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    submitted_at=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    grade=models.FloatField(null=True,blank=True)

class InputOutput(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    input_data=models.TextField()
    expected_output=models.TextField()


class Enrollment(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    enrolled_at=models.DateTimeField(auto_now_add=True)