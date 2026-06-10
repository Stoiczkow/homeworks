import time

from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)

from django.core.cache import cache

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework.decorators import api_view
from .models import Task, Place, PlaceArchive
from .serializers import TaskSerializer, PlaceSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.db import transaction

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from .tasks import simulate_cpu_bound_task, multiply

import redis

class TaskViewSet(viewsets.ModelViewSet):
    '''
    Widok obsługuje cały CRUD
    '''
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    @method_decorator(cache_page(60 * 5, key_prefix="tasks"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PlaceListAndCreateView(ListCreateAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all().order_by('-created_at')

    @method_decorator(cache_page(60 * 5, key_prefix="places"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class PlaceGetSingleView(RetrieveAPIView):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    lookup_field = "id"

class PlaceDeleteApiView(DestroyAPIView):
    queryset = Place.objects.all()
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        with transaction.atomic():
            place = Place.objects.get(id=kwargs["id"])
            PlaceArchive.objects.create(name=place.name, description=place.description)

            # Symulacja błędu:
            error_example = 2 / 0
            
            place.delete()

        return Response({"message": "Data Archived"})


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
    data_key = "big_data"

    data = cache.get(data_key)

    if data:
        return Response(data)
    else:
        time.sleep(3)
        data = {"data": "complex_data"}
        cache.set(data_key, data, 60 * 5)
        return Response(data)
    
@api_view(["GET"])
def test_celery(request):

    a = int(request.query_params.get("a"))
    b = int(request.query_params.get("b"))

    task = multiply.delay(a, b)

    return Response(
        {"message": "Zadanie jest w trakcie wykonywania", "task_id": task.id}
    )
    # r = redis.Redis(host='localhost', port=6379)
    # print(r.ping())
    # return Response("Odp")