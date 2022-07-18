from django.urls import path
from .views import api_overview, task_list, delete_task, create_task, task_update

urlpatterns = [
    path('', api_overview ),
    path('tasks/', task_list ),
    path('tasks/create/', create_task ),
    path('tasks/task/update/<pk>/', task_update ),
    path('tasks/delete/<pk>/', delete_task )
]