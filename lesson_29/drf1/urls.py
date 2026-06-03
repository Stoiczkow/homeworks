"""
URL configuration for drf1 project.

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

from tasks.views import (
    TaskViewSet, 
    PlaceListAndCreateView,
    PlaceGetSingleView,
    complex_view, 
    test_celery,
    hello_celery,
    log_view,
    task_start,
    task_status
    )
from products.views import ProductViewSet, NoteViewSet, AuthorViewSet, BookViewSet, hello_view, set_name, calculator

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'products', ProductViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('api/set-name/', set_name),
    path('api/hello/', hello_view),
    path('api/calculate/', calculator),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path("api/places/", PlaceListAndCreateView.as_view()),
    path("api/places/<int:id>", PlaceGetSingleView.as_view()),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/complex", complex_view),
    path("test_celery/", test_celery),
    path("hello_celery/", hello_celery),
    path("log_timestamp/", log_view),
    path("task-start/", task_start),
    path("task-status/", task_status)
]
