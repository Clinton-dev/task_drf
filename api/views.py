from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List':'/tasks/',
        'Create': 'tasks/create/',
        'Detail': 'tasks/task/detail/<pk>/',
        'Delete': 'tasks/delete/<pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    """
    List all tasks
    """
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# Todo build:  detail, create and delete endpoints
@api_view(['PUT'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task deleted successfully!!")