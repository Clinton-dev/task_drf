from django.urls import path
from .views import api_overview,task_list, delete_task, create_task

urlpatterns = [
    path('', api_overview ),
    path('tasks/', task_list ),
    path('tasks/create/', create_task ),
    path('tasks/delete/<pk>/', delete_task )
]