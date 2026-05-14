from django.urls import path
from rest_framework.routers import DefaultRouter

from .api_views import BookViewSet, ReservationListCreateAPIView

router = DefaultRouter()
router.register('books', BookViewSet, basename='api-books')

urlpatterns = router.urls + [
    path('reservations/', ReservationListCreateAPIView.as_view(), name='api-reservations'),
]