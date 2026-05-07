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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from article.views import create_article, filter_articles, view_categories, category_detail_view
from blog.views import home_blog, posts_in_category_list

urlpatterns = [
    path('', RedirectView.as_view(url='/blog', permanent=False)),
    path('admin/', admin.site.urls),
    path('article/', create_article),
    path('filter_article', filter_articles),
    path('categories/', view_categories),
    path('categories/<int:category_id>', category_detail_view),

    path('blog/', home_blog),
    path('blog/category/<int:category_id>', posts_in_category_list),

    path('accounts/', include('allauth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)