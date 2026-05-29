from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Artykul
from .serializers import ArtkulSerializer

RETRIEVE_CACHE_TIMEOUT = 60        # 1 minuta
LIST_CACHE_TIMEOUT = 60 * 10       # 10 minut
RETRIEVE_CACHE_KEY = 'artykul_retrieve_{pk}'


# Zadanie 8 + Zadanie 9 – ViewSet z różnymi czasami cache dla list i retrieve,
# z unieważnianiem cache po aktualizacji obiektu
class ArtkulViewSet(viewsets.ModelViewSet):
    queryset = Artykul.objects.all()
    serializer_class = ArtkulSerializer

    # Zadanie 8 – lista cachowana na 10 minut przez dekorator cache_page
    @method_decorator(cache_page(LIST_CACHE_TIMEOUT))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # Zadanie 8 + 9 – szczegóły cachowane na 1 minutę z własnym kluczem,
    # dzięki czemu można je precyzyjnie unieważnić po aktualizacji
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        cache_key = RETRIEVE_CACHE_KEY.format(pk=pk)

        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)
        cache.set(cache_key, response.data, RETRIEVE_CACHE_TIMEOUT)
        return response

    # Zadanie 9 – unieważnienie cache szczegółów po aktualizacji obiektu
    def perform_update(self, serializer):
        instance = serializer.save()
        cache_key = RETRIEVE_CACHE_KEY.format(pk=instance.pk)
        cache.delete(cache_key)

    # create i destroy nie są cachowane – brak nadpisania, działa domyślnie
