from django.core.cache import cache, caches
from django.test import RequestFactory
from django.utils.cache import _generate_cache_header_key, _generate_cache_key


def _delete_view_cache(path, key_prefix):
    request = RequestFactory().get(path, HTTP_HOST='testserver')
    default_cache = caches['default']
    header_key = _generate_cache_header_key(key_prefix, request)
    header_list = default_cache.get(header_key)

    if header_list is not None:
        response_key = _generate_cache_key(request, 'GET', header_list, key_prefix)
        default_cache.delete(response_key)

    default_cache.delete(header_key)


def invalidate_product_detail_cache(product_id):
    _delete_view_cache(f'/api/products/{product_id}/', 'product-detail')


def invalidate_product_list_caches():
    _delete_view_cache('/api/products/', 'products-list')
    _delete_view_cache('/api/products-cached/', 'products-cached-view')
    cache.delete('expensive_product_analysis')
    caches['filebased'].delete('filebased_product_snapshot')


def invalidate_all_product_related_caches():
    invalidate_product_list_caches()