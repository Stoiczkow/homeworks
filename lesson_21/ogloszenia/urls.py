from django.urls import path
from . import views
from .views import category_list_view

urlpatterns = [
    path("info/", views.info_view, name="info"),
    path("user/<str:username>/", views.user_profile_view, name="user-profile"),
    path("categories/", category_list_view, name="category-list"),
]