import time

from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView


from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema


from .models import Task, Place, PlaceArchive
from .serializers import TaskSerializer, PlaceListCreateSerializer
from django.db import transaction

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .tasks import simulate_cpu_bound_task, multiplay


class TaskViewSet(viewsets.ModelViewSet):
    """
    widok obłsuguje cały CRUD
    """
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

class PleaceDeleteView(DestroyAPIView):
    queryset = Place.objects.all()
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        
        with transaction.atomic():
            place = Place.objects.get(id=kwargs["id"])
            PlaceArchive.objects.create(name=place.name,
                                        description = place.description)
            # Symulacja wystąpienia błędu
            divide_error = 2 / 0
            place.delete()
            return Response({"message": "Data archived"})

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


@api_view(["GET"])
def complex_view(request):
    data_key = "big_data"

    data = cache.get(data_key)

    if data:
        return Response(data)
    
    else:
        #symulacja długiej operacji
        time.sleep(5)
        data = {"data": "complex data"}
        cache.set(data_key, data, 60*5)
        return Response(data)
    
    # Ręczna metoda powyżej cahse lepiej bo nie są to nadmiarowe dane


@api_view(["GET"])
def calculate_view(request):
    num1 = request.query_params.get("num1")
    num2 = request.query_params.get("num2")
    operation = request.query_params.get("operation")

    if num1 is None or num2 is None or operation is None:
        return Response(
            {"detail": "Wymagane parametry: num1, num2, operation."},
            status=400,
        )

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return Response(
            {"detail": "Parametry num1 i num2 muszą być liczbami."},
            status=400,
        )

    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return Response(
                {"detail": "Dzielenie przez zero jest niedozwolone."},
                status=400,
            )
        result = num1 / num2
    else:
        return Response(
            {"detail": "Niepoprawna operacja. Użyj: add, subtract, multiply, divide."},
            status=400,
        )

    return Response({"result": result})
    
@api_view(["GET"])
def test_celery(request):
    a = request.query_params.get("a")
    b = request.query_params.get("b")
    print(int(a), int(b))
    # task = simulate_cpu_bound_task.delay(20)
    task = multiply.delay(int(a), int(b)) # w delay zawsze przekazujemy paremetry
    return Response(
        {"message": "Zadanie jest w trakcie wykonywania", "task_id": task.id}
    )

# albo uruchamiamy zawsze albo uruchamiamy za żądanie w tle
