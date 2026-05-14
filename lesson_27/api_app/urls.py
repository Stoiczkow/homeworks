from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, cached_product_list_view, file_cache_probe_view, performance_dashboard_view

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')

urlpatterns = router.urls + [
    path('products-cached/', cached_product_list_view, name='products-cached'),
    path('performance/', performance_dashboard_view, name='performance-dashboard'),
    path('file-cache/', file_cache_probe_view, name='file-cache-probe'),
]