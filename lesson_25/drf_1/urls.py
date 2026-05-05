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
from drf_spectacular.views import (
SpectacularAPIView,
SpectacularSwaggerView,
SpectacularRedocView,
)
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from tasks.views import (
    TaskViewSet,
    PlaceListAndCreateView,
    PlaceGetSingleView,
    complex_view,
    PleaceDeleteView,
    calculate_view,
)

from products.views import ProductsViewSet, setname, helloview, NoteViewSet, AuthorViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'products', ProductsViewSet)
router.register(r"notes", NoteViewSet)
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path("api/set-name/", setname),
    path("api/hello/", helloview),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path("api/places/", PlaceListAndCreateView.as_view()),
    path("api/places/<int:id>/", PlaceGetSingleView.as_view()),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/complex/", complex_view),
    path("api/calculate/", calculate_view),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/",SpectacularSwaggerView.as_view(url_name="schema"),name="swagger-ui",),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),name="redoc",),
    path("api/places/delete/<int:id>", PleaceDeleteView.as_view()),
]