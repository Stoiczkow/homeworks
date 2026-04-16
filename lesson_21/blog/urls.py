from django.urls import path
from . import views

urlpatterns = [
    # Zadanie 3
    path('categories/', views.category_list_view, name='category-list'),
    # Zadanie 6
    path('categories/<int:pk>/', views.category_detail_view, name='category-detail'),
    # Zadanie 8 + 10
    path('articles/', views.article_list_view, name='article-list'),
]