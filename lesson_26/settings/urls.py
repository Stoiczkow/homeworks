from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.tasks.views import TaskViewSet, PlaceListAndCreateView, PlaceGetSingleView
from apps.products.views import (
    ProductViewSet,
    hello_view,
    set_name,
    CurrentUserView,
    NoteViewSet,
    BookViewSet,
    AuthorViewSet,
    calculate
)

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'products', ProductViewSet, basename='products')
router.register(r'notes', NoteViewSet)
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/hello/', hello_view),
    path('api/set-name/', set_name),
    path('api/calculate/', calculate),
    path('api/me/', CurrentUserView.as_view(), name="current-user"),
    path('api/places/', PlaceListAndCreateView.as_view()),
    path('api/places/<int:id>', PlaceGetSingleView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]
