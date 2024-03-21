from django.contrib import admin
from django.urls import path

from tasks_list.views import (TaskCreateView, TaskDeleteView, TasksListView,
                              TaskUpdateView)

app_name = 'tasks_list'

urlpatterns = [
    path('', TasksListView.as_view(), name='index'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('task-create/', TaskCreateView.as_view(), name='task_create'),
]
