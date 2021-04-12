from rest_framework import serializers
from Tasks.models import Task, Bucket


class BucketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bucket
        fields = (
            'id',
            'title',
            'menger',
            'created',
        )


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'assigner',
            'bucket',
            'created',
            'modified',
            'done',
        )

