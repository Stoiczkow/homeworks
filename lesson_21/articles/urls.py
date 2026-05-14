from django.urls import path

from . import views


urlpatterns = [
    path('', views.article_list_view, name='article-list'),
    path('articles/', views.article_list_view, name='article-list-alt'),
    path('categories/', views.category_list_view, name='category-list'),
    path('categories/<int:pk>/', views.category_detail_view, name='category-detail'),
]