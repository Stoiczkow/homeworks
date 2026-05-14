from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('category/<int:category_id>/', views.category_posts_view, name='category-posts'),
]