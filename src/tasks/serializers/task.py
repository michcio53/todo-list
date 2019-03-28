from rest_framework import serializers
from tasks.models import Task
from core.serializers.user_basic_serializer import UserBasicSerializer
from django.utils.timezone import now


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'done_date',
            'task_status',
        ]


class ListTaskSerializer(serializers.ModelSerializer):
    user = UserBasicSerializer(read_only=True)
    is_delayed = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id',
            'user',
            'name',
            'description',
            'done_date',
            'task_status',
            'is_delayed',
        ]

    def get_is_delayed(self, obj):
        return now() > obj.done_date


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'task_status',
        ]

