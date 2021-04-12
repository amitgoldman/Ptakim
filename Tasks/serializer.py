from rest_framework import serializers
from Tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'owner',
            'user',
            'created',
            'modified',
            'done',
        )

