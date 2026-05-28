from .views import ProtectedView, cache_test, selective_cache_test, CachedItemViewSet
from django.urls import path, include
from rest_framework import routers



router = routers.DefaultRouter()
router.register('cached-item', CachedItemViewSet, basename='cached-item')
urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('cache_test/', cache_test, name="cache_test"),
    path('selective_cache_test/', selective_cache_test, name="selective-cache-test"),
    path('', include(router.urls)),
]

