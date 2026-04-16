"""
URL configuration for projekt_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from article.views import create_article, filter_articles, category_view, category_detail_view
from blog.views import posts_from_category, home, profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', create_article),
    path("filter_article/", filter_articles),
    path("categories/", category_view),
    path("categories/<int:category_id>", category_detail_view),
    path("category/<int:category_id>", posts_from_category),
    path("blog/home", home),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', profile_view)
]
