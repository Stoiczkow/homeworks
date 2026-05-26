from django.urls import path
from .views import ProfilView

urlpatterns = [
    path('profil/', ProfilView.as_view(), name='profil'),
]
