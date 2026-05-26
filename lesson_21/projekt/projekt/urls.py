from django.contrib import admin
from django.urls import path
from article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', views.create_article),
    path('articles/', views.article_list_view, name='article-list'),
    path('filter_article/', views.filter_article),
    path('categories/', views.category_list_view, name='category-list'),
    path('categories/<int:pk>/', views.category_detail_view, name='category-detail'),
]
