"""
URL configuration for drf_1 project.

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
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
    )

from tasks.views import (
    TaskViewSet, 
    PlaceListAndCreateView, 
    PlaceGetSingleView, 
    complex_view,
    PlaceDeleteView,
    test_celery,
    multiply_view,
    test_hello
    )
from products.views import (
    ProductViewSet, 
    setname, 
    helloview, 
    NoteViewSet, 
    AuthorViewSet, 
    BookViewSet, 
    calculate)

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'products', ProductViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    
    path('api/hello/', helloview),
    path('api/set-name/', setname),
    path('api/calculate/', calculate),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path('api/places/', PlaceListAndCreateView.as_view()),
    path('api/places/<int:id>/', PlaceGetSingleView.as_view()),
    path('__debug__/', include("debug_toolbar.urls")),
    path('api/complex/', complex_view),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path('api/places/delete/<int:id>', PlaceDeleteView.as_view()),
    path('test_celery/', test_celery),
    path('multiply/a/b/', multiply_view),
    path('hello-celery/', test_hello)

]