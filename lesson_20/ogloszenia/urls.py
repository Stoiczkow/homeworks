from django.urls import path
from . import views

urlpatterns = [
    path("info/", views.info_view, name="info"),
    path("user/<str:username>/", views.user_profile_view, name="user-profile"),
]