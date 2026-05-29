from rest_framework.routers import DefaultRouter
from .views import ArtkulViewSet

router = DefaultRouter()
router.register('artykuly', ArtkulViewSet, basename='artykul')

urlpatterns = router.urls
