from django.shortcuts import render
from Tasks.serializer import TaskSerializer
from rest_framework.decorators import action
from rest_framework import viewsets, filters
from Tasks.models import Task, TaskList


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    @action(detail=True, methods=['patch'], permission_classes=[])
    def change_user(self, request, pk=None):
        task = self.get_object()
        print(request.user, task.owner)
        pass


class TaskListViewSet(viewsets.ModelViewSet):
    queryset = TaskList.objects.all()
    serializer_class = TaskSerializer

