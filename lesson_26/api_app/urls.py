from django.urls import path

from .views import ProtectedUserView

urlpatterns = [
    path('protected/', ProtectedUserView.as_view(), name='protected-user'),
]