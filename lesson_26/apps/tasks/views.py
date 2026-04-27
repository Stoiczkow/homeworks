from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from apps.tasks.models import Task, Place
from apps.tasks.serializers import TaskSerializer, PlaceListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer


class PlaceListAndCreateView(ListCreateAPIView):
    serializer_class = PlaceListSerializer
    queryset = Place.objects.all().order_by('-created_at')


class PlaceGetSingleView(RetrieveUpdateAPIView):
    serializer_class = PlaceListSerializer
    queryset = Place.objects.all()
    lookup_field = "id"

