from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Course, Module, Task, Submission, InputOutput, Enrollment


class RegisterSerializer(serializers.ModelSerializer):
   class Meta:
       model=User
       fields=['username','password']

   def create(self,validate_data):
       user=User.objects.create_user(
        username=validate_data['username'],
        password=validate_data['password']
       )
       return user  
   


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

class CourseSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class InputOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputOutput
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'