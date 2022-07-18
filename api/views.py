from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def task_list(request):
    """
    List all tasks
    """
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, safe=False)

# Todo build: create and delete endpoints

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