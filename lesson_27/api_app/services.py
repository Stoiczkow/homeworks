import time

from django.conf import settings
from django.core.cache import cache, caches
from django.db.models import Avg

from .models import Product


def get_expensive_product_analysis():
    cache_key = 'expensive_product_analysis'
    result = cache.get(cache_key)

    if result is None:
        time.sleep(3)
        average_price = Product.objects.aggregate(avg_price=Avg('price'))['avg_price'] or 0
        result = {
            'average_price': float(average_price),
            'product_count': Product.objects.count(),
            'source': 'Obliczone na żywo',
        }
        cache.set(cache_key, result, timeout=300)
    else:
        result = {**result, 'source': 'Pobrane z cache'}

    return result


def get_filebased_product_snapshot():
    file_cache = caches['filebased']
    cache_key = 'filebased_product_snapshot'
    result = file_cache.get(cache_key)

    if result is None:
        result = {
            'product_names': list(Product.objects.order_by('id').values_list('name', flat=True)),
            'cache_backend': 'FileBasedCache',
            'cache_directory': str(settings.BASE_DIR / 'django_cache'),
            'source': 'Zapisane do cache plikowego',
        }
        file_cache.set(cache_key, result, timeout=600)
    else:
        result = {**result, 'source': 'Odczytane z cache plikowego'}

    return result