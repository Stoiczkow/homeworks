from rest_framework import viewsets
import time

from django.core.cache import cache

from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from  rest_framework.generics import DestroyAPIView
from django.db import transaction

from urllib3 import request

from .models import Place, Task, Note, PlaceArchive
from .serializers import TaskSerializer, NoteSerializer
from django.utils.decorators import method_decorator

from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from .tasks import multiply, simulate_cpu_bound_task, hello_world, log_timestamp, count_users, update_user_last_login, video_task
from django.http import HttpResponse


def run_task(request):
    hello_world.delay()

    return HttpResponse("Task został wysłany!")

class TaskViewSet(viewsets.ModelViewSet):
    """
    Widok zestawu zadań, który obsługuje operacje CRUD na modelu Task. Używa serializer TaskSerializer do konwersji danych i wymaga uwierzytelnienia JWT do dostępu. Dodatkowo, metoda list jest cache'owana na 5 minut, aby poprawić wydajność przy dużej liczbie zapytań.

    Args:
        viewsets (_type_): _description_

    Returns:
        _type_: _description_
    """
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    @method_decorator(cache_page(60*5))
    def list(self, request, *args, **kwargs):


        return super().list(request, *args, **kwargs)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    # serializer_class = Product.O
    permission_classes = [IsAuthenticated]

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
        return Response( data)
    else:
        #simulate a long-running operation
        time.sleep(5)
        data = {"data": "complex data"}
        cache.set(data_key, data, timeout=60*5)

        return Response(data)
    

class PlaceDeleteView(DestroyAPIView):
    queryset = Place.objects.all()
    lookup_field = 'id'
    
    def delete(self, request, *args, **kwargs):
        with transaction.atomic():
            place = Place.objects.get(id=place_id)
            PlaceArchive.objects.create(
                name=place.name,
                description=place.description
            )

            # divide_by_zero = 1 / 0 #symulacja bledu tranzakcji
            place.delete()
        return Response({"message": "Data archived and deleted successfully."}, status=204)


@api_view(["GET"])
def test_celery(request):
    # task = simulate_cpu_bound_task.delay(20)
    a = request.query_params.get('a')
    b = request.query_params.get('b')

    task = multiply.delay(int(a), int(b))

    return Response(
        {"message": "Zadanie jest w trakcie wykonywania", "task_id": task.id}
    )



@api_view(['GET'])
def test_log(request):

    log_timestamp.delay()

    return Response({
        "message": "Timestamp został zapisany"
    })


@api_view(['GET'])
def count_users_view(request):

    task = count_users.delay()

    return Response({
        "message": "Liczenie użytkowników uruchomione",
        "task_id": task.id
    })

@api_view(['GET'])
def update_user_last_login_view(request, user_id):

    update_user_last_login.delay(user_id)

    return Response({
        "message": f"Zadanie aktualizacji ostatniego logowania dla użytkownika {user_id} uruchomione",
        "user_id": user_id
    })


@api_view(['GET'])
def test_video_task(request):

    video_task.delay()

    return Response({
        "message": "Zadanie przetwarzania wideo uruchomione"
    })

