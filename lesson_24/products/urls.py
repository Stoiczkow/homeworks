from django.urls import path

from products.views import RegisterView

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
]