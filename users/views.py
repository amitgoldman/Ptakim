from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from Tasks.models import Task, Bucket
from Tasks.serializer import TaskSerializer, BucketSerializer
from users.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def tasks(self, request, pk=None):
        queryset = Task.objects.filter(assigner=pk)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def buckets_own(self, request, pk=None):
        queryset = Bucket.objects.filter(menger=pk)
        serializer = BucketSerializer(queryset, many=True)
        return Response(serializer.data)
