from django.shortcuts import render
from Tasks.serializer import TaskSerializer
from rest_framework import viewsets
from Tasks.models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
