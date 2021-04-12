from rest_framework import serializers
from Tasks.models import Task, Bucket


class BucketSerializer(serializers.ModelSerializer):
    tasks_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Bucket
        fields = (
            'id',
            'title',
            'menger',
            'created',
            'tasks_count'
        )

    def get_tasks_count(self, obj) -> int:
        return Task.objects.filter(bucket__id=obj.id).count()


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

