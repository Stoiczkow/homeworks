from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.models import Product
from apps.products.serializers import ProductSerializer
from apps.products.services import get_expensive_calculation


def _retrieve_cache_key(pk):
    return f'product:retrieve:{pk}'


RETRIEVE_TTL = 60


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Zadanie 8: list cachowany na 10 minut przez @cache_page
    @method_decorator(cache_page(60 * 10))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # Zadanie 9: retrieve - manualny cache z deterministycznym kluczem,
    # zeby mozna bylo go usunac po update/destroy.
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        cache_key = _retrieve_cache_key(pk)
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)

        response = super().retrieve(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=RETRIEVE_TTL)
        return response

    def perform_update(self, serializer):
        super().perform_update(serializer)
        cache.delete(_retrieve_cache_key(serializer.instance.pk))

    def perform_destroy(self, instance):
        pk = instance.pk
        super().perform_destroy(instance)
        cache.delete(_retrieve_cache_key(pk))


# Zadanie 7: selektywne cachowanie - cache tylko dla drogich obliczen,
# szybkie zapytanie do bazy wykonuje sie za kazdym razem.
@api_view(['GET'])
def dashboard(request):
    fast_data = {
        'product_count': Product.objects.count(),
    }
    expensive_data = get_expensive_calculation()
    return Response({
        'fast': fast_data,
        'expensive': expensive_data,
    })
