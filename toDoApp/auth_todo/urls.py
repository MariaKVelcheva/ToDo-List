from django.urls import path

from toDoApp.auth_todo import views

urlpatterns = [
    path('', views.ToDoListCreateAPIView.as_view(), name='task-list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('categories/', views.CategoriesListAPIView.as_view(), name='category-list'),
]