from rest_framework import serializers

from toDoApp.auth_todo.models import Category, Task
from toDoApp.profiles.serializers import UserModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']


class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    assignees = UserModelSerializer(many=True, read_only = True)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'category', 'assignee', ]

