import time

from rest_framework.response import Response
from django.http import HttpResponse
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateAPIView, 
    CreateAPIView, 
    DestroyAPIView
    )

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.db import transaction

from .models import Task, Place, PlaceArchive
from .serializers import TaskSerializer, PlaceListCreateSerializer
from .tasks import simulate_cpu_bound_task,multiply, hello_world



class TaskViewSet(viewsets.ModelViewSet):
    """
    Widok obsługuje cały CRUD
    """


    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    @method_decorator(cache_page(60 * 10))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 1))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class PlaceListAndCreateView(ListCreateAPIView):
    serializer_class = PlaceListCreateSerializer
    queryset = Place.objects.all().order_by('-created_at')

class PlaceGetSingleView(RetrieveUpdateAPIView):
    serializer_class = PlaceListCreateSerializer
    queryset = Place.objects.all().order_by('-created_at')
    lookup_field = "id"

class PlaceDeleteView(DestroyAPIView):
    queryset = Place.objects.all()
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        with transaction.atomic():
            place = Place.objects.get(id=kwargs["id"])
            PlaceArchive.objects.create(name=place.name, description=place.description)
            place.delete()
            return Response({"message": "Data archived"})

        # return super().delete(request, *args, **kwargs)

@extend_schema(
    summary="Pobierz szczegóły jednego produktu",
    description="Zwraca pełne informacje o produkcie na podstawie jego ID.",
    tags=["Produkty"],
    parameters=[
        OpenApiParameter(
            name="category",
            description="Filtruj produkty po ID kategorii",
            required=False,
            type=OpenApiTypes.INT,
        ),
    ], # Grupuje endpointy w UI
)


@api_view(['GET'])
def complex_view(request):
    data_key = 'big_data'

    data = cache.get(data_key)

    if data:
        return Response(data)
    else:
        time.sleep(5)
        data = {"data": "complex data"}
        cache.set(data_key, data, 60 * 5)
        return Response(data)


@api_view(["GET"])
def test_celery(request):
    task = simulate_cpu_bound_task.delay(20)
    return Response(
        {"message": "Zadanie jest w trakcie wykonywania", "task_id": task.id}
    )

@api_view(["GET"])
def multiply_view(request):
    a = request.query_params.get("a")
    b = request.query_params.get("b")

    task = multiply.delay(int(a), int(b))
    return Response(
        {"message": "Zadanie jest w trakcie wykonywania", "task_id": task.id}
    )

def test_hello(request):
    hello_world.delay()
    return HttpResponse("Zadanie zostało dodane do kolejki!")