import time

from django.core.cache import cache
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import CachedItem
from .serializers import CachedItemSerializer
from django.utils.decorators import method_decorator



class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Masz dostęp do chronionego endpointu",
            "username": request.user.username,
        })

@cache_page(60)
@api_view(["GET"])
def cache_test(request):
    print("Widok cache_test wykonał się naprawde")
    
    time.sleep(2)

    return Response({
        "messege": "To jest odpowiedź testowa",
        "generated_at": time.strftime("%H:%M:%S"),
        "info": "Jeśli cache działa kolejne odświeżenie będzie szybsze",
    })

@api_view(["GET"])
def selective_cache_test(request):
    print("Widok selective_cache_test wykonał się naprawede")

    fast_data = {
        "message": "To jest szybka część odpowiedzi",
        "gerated_at": time.strftime("%H:%M:%S"),
    }

    cache_key = "expensive_calculation_result"

    expensive_data = cache.get(cache_key)

    if expensive_data is None:
        print("Brak w cache wykonuje drugie obliczenie")
        time.sleep(3)

        expensive_data = {
            "result": 42,
            "source": "Obliczone na żywo",
            "calculated_at": time.strftime("%H:%M:%S"),
        }

        cache.set(cache_key, expensive_data, 60)
    else:
        print("Znaleziono w cache")
        expensive_data["source"] = "Pobrane z cache"

    return Response({
        "fast_data": fast_data,
        "expensive_data": expensive_data,
    })

# Zadanie 8
class CachedItemViewSet(viewsets.ModelViewSet):
    queryset = CachedItem.objects.all()
    serializer_class = CachedItemSerializer

    @method_decorator(cache_page(60 * 10))
    def list(self, request, *args, **kwargs):
        print("LIST się wykonał")
        return super().list(request, *args, **kwargs)
    
    @method_decorator(cache_page(60))
    def retrieve(self, request, *args, **kwargs):
        print("retrive się wykonał")
        return super().retrieve(request, *args, **kwargs)
