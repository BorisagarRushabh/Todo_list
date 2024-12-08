from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from base.models import Task
from .serializers import TaskSerializer


@api_view(["GET"])
def getAllTask(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getOneTask(request):
    serializer = TaskSerializer(data=request.data)
    serializer = TaskSerializer(
        Task.objects.filter(
            Title=serializer.initial_data.get("title")), many=True
    )
    return Response(serializer.data)


@api_view(["POST"])
def addNewTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("Invalid")


@api_view(["PUT", "DELETE"])
def updateTask(request, pk):
    try:
        task_id = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = TaskSerializer(task_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        task_id.delete()
        return Response("user deleted", status=status.HTTP_204_NO_CONTENT)
