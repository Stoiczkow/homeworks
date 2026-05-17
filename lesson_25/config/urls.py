"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from products.views import ProductViewSet, set_name, hello, NoteViewSet, calculate, AuthorViewSet, BookViewSet


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'notes', NoteViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/set-name/', set_name),
    path('api/hello/', hello),
    path('api/calculate/', calculate),
    path('api/', include(router.urls)),
]

