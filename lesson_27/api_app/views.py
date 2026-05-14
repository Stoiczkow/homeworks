from django.conf import settings
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .cache_utils import invalidate_all_product_related_caches, invalidate_product_detail_cache, invalidate_product_list_caches
from .models import Product
from .serializers import ProductSerializer
from .services import get_expensive_product_analysis, get_filebased_product_snapshot


def home_view(request):
	return render(
		request,
		'home.html',
		{
			'cache_dir': settings.BASE_DIR / 'django_cache',
		},
	)


@cache_page(60, key_prefix='products-cached-view')
@api_view(['GET'])
def cached_product_list_view(request):
	products = Product.objects.all().order_by('id')
	serializer = ProductSerializer(products, many=True)
	return Response(
		{
			'generated_at': timezone.now().isoformat(),
			'source': 'Widok wygenerowany na żywo i zapisany do cache na 60 sekund.',
			'products': serializer.data,
		}
	)


@api_view(['GET'])
def performance_dashboard_view(request):
	latest_product = Product.objects.order_by('-updated_at').first()
	quick_database_data = {
		'product_count': Product.objects.count(),
		'latest_product': latest_product.name if latest_product else None,
	}

	return Response(
		{
			'quick_database_data': quick_database_data,
			'expensive_analysis': get_expensive_product_analysis(),
		}
	)


@api_view(['GET'])
def file_cache_probe_view(request):
	return Response(get_filebased_product_snapshot())


class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all().order_by('id')
	serializer_class = ProductSerializer

	@method_decorator(cache_page(60 * 10, key_prefix='products-list'))
	def list(self, request, *args, **kwargs):
		return super().list(request, *args, **kwargs)

	@method_decorator(cache_page(60, key_prefix='product-detail'))
	def retrieve(self, request, *args, **kwargs):
		return super().retrieve(request, *args, **kwargs)

	def perform_create(self, serializer):
		serializer.save()
		invalidate_all_product_related_caches()

	def perform_update(self, serializer):
		product = serializer.save()
		invalidate_product_detail_cache(product.pk)
		invalidate_product_list_caches()

	def perform_destroy(self, instance):
		product_id = instance.pk
		instance.delete()
		invalidate_product_detail_cache(product_id)
		invalidate_product_list_caches()
