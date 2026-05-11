from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.products.views import ProductViewSet, dashboard

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/dashboard/', dashboard, name='dashboard'),
    path('__debug__/', include('debug_toolbar.urls')),
]
