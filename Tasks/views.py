from rest_framework.permissions import IsAuthenticated, IsAdminUser

from Tasks.access import TaskPolicy
from Tasks.serializer import TaskSerializer, BucketSerializer
from rest_framework.decorators import action
from rest_framework import viewsets, filters, permissions
from rest_framework.response import Response
from Tasks.models import Task, Bucket


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = (TaskPolicy,)

    @action(detail=True, methods=['post'])
    def update_done(self, request, pk=None):
        task = self.get_object()
        if "done" in request.data:
            task.done = request.data["done"]
        else:
            task.done = not task.done
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class BucketViewSet(viewsets.ModelViewSet):
    queryset = Bucket.objects.all()
    serializer_class = BucketSerializer

    @action(detail=True, methods=['get'])
    def tasks(self, request, pk=None):
        queryset = Task.objects.filter(bucket_id=pk)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
