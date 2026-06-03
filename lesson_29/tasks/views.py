from curses import keyname
import time
from django.core.cache import cache
from celery.result import AsyncResult
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
    DestroyAPIView
)
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Task, Place
from .serializers import TaskSerializer, PlaceListCreateSerializer
from .tasks import simulate_cpu_bound_task, multiply, hello_world, log_timestamp, simulate_processing_video, do_operation


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by("-created_at")
    serializer_class = TaskSerializer

    @method_decorator(cache_page(60 * 5, key_prefix="tasks"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PlaceListAndCreateView(ListCreateAPIView):
    serializer_class = PlaceListCreateSerializer
    queryset = Place.objects.all().order_by("-created_at")

    @method_decorator(cache_page(60 * 5, key_prefix="places"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PlaceGetSingleView(RetrieveUpdateAPIView):
    serializer_class = PlaceListCreateSerializer
    queryset = Place.objects.all()
    lookup_field = "id"
    
@api_view(['GET'])
def complex_view(request):
    data_key = 'big_data'
    
    data = cache.get(data_key)
    
    if data:
        return Response(data)
    else:
        #symulacja długiej operacji
        time.sleep(5)
        data = {"data": "complex_data"}
        cache.set(data_key, data, 60 * 5)
        return Response(data)
    
@api_view(["GET"])
def test_celery(request):
    a = request.query_params.get("a")
    b = request.query_params.get("b")
    
    #task = simulate_cpu_bound_task.delay(20)
    task = multiply.delay(int(a), int(b))
    return Response(
        {"message": "mnożenie jest w trakcie wykonywania", "task_id": task.id}
    )
    
    
@api_view(["GET"])
def hello_celery(request):    
    task = hello_world.delay()
    
    return Response(
        {"message": "Zadanie Hello world jest w trakcie...", "task_id": task.id}
    )
    
@api_view(["GET"])
def log_view(request):    
    task = log_timestamp.delay()
    return Response(
        {"message": "zapis do pliku w trakcie", 
         "task_id": task.id}
    )
    
@api_view(["GET"])
def process_video(request):    
    task = simulate_processing_video.delay()
    return Response(
        {"message": "Przetwarzanie wideo rozpoczęte!", 
         "task_id": task.id}
    )

@api_view(["GET"])
def task_start(request):  
    task = do_operation.delay()
    
    return Response(
        {"message": "Task started...", 
         "task_id": task.id}
    )
    
@api_view(["GET"])
def task_status(request):
    task_id = request.query_params.get("task_id")

    task = AsyncResult(task_id)

    if task.state == "PROGRESS":
        return Response({
            "state": task.state,
            "current": task.info["current"],
            "total": task.info["total"]
        })

    return Response({
        "state": task.state,
        "result": task.result
    })