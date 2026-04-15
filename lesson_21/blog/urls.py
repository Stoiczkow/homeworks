from django.urls import path
from .views import CategoryListView, CategoryDetailView, ArticleListView

urlpatterns = [
    # Zadanie 3
    path('categories/', CategoryListView.as_view(), name='category-list'),
    # Zadanie 6
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # Zadanie 8 + 10
    path('articles/', ArticleListView.as_view(), name='article-list'),
]