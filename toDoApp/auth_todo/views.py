from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from toDoApp.auth_todo.models import Task, Category
from toDoApp.auth_todo.serializers import TaskSerializer, CategorySerializer


class ToDoListCreateAPIView(ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()

        category = self.request.query_params.get('category')
        state = self.request.query_params.get('state')

        if category:
            queryset = queryset.filter(category__id=category)
        if state:
            queryset = queryset.filter(state=state.lower())

        return queryset


class CategoriesListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



