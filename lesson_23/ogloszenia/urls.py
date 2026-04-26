from django.urls import path
from . import views
from .views import category_list_view, category_detail_view, latest_ogloszenia_view

urlpatterns = [
    path("info/", views.info_view, name="info"),
    path("user/<str:username>/", views.user_profile_view, name="user-profile"),
    path("categories/", category_list_view, name="category-list"),
    path("category/<int:category_id>/", category_detail_view, name="category-detail"),
    path("latest/", latest_ogloszenia_view, name="latest_ogloszenia"),
]