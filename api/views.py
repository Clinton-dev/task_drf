from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from api.models import Task
from api.serializers import TaskSerializer

@csrf_exempt
def task_list(request):
    """
    List all tasks
    """
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)

