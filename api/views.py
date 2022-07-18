from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import Response
from .models import Task
from .serializers import TaskSerializer

@csrf_exempt
def task_list(request):
    """
    List all tasks
    """
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, safe=False)

# Todo build: create and delete endpoints

def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task deleted successfully!!")