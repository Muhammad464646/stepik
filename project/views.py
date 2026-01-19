from django.shortcuts import render
from rest_framework import viewsets, permissions,generics
from .models import Course, Module, Task, Submission, InputOutput, Enrollment
from .serializers import CourseSerializer, ModuleSerializer, TaskSerializer, SubmissionSerializer, InputOutputSerializer, EnrollmentSerializer,RegisterSerializer
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

class InputOutputViewSet(viewsets.ModelViewSet):
    queryset = InputOutput.objects.all()
    serializer_class = InputOutputSerializer
    permission_classes = [permissions.IsAuthenticated]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegisterViewSet(generics.CreateAPIView):
    serializer_class=RegisterSerializer
    permission_classes=[permissions.AllowAny]