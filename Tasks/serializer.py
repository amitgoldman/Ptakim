from rest_framework import serializers
from Tasks.models import Task, TaskList


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskList
        fields = (
            'title',
            'menger',
            'created',
        )


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'assigner',
            'task_list',
            'created',
            'modified',
            'done',
        )

