from django.contrib import admin
from django.urls import path, include
from app_Article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('category/<int:category_id>/', views.articles_by_category, name='articles_by_category'),
    path('author/<int:author_id>/', views.articles_by_author, name='articles_by_author'),
    path('accounts/', include('allauth.urls')),
]
