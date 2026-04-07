"""
URL configuration for core project.

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
from django.urls import path

from product.views import InfoView, RulesView, UserView, ProductView, ProductCreateFormView, CategoryProductFilter
from note.views import NoteListView, NoteDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', InfoView.as_view(), name='info-view'),
    path('rules/', RulesView.as_view(), name='rules-view'),
    path('user/<str:username>', UserView.as_view(), name='user-view'),
    path('products/', ProductView.as_view(), name='products-view'),
    path('product/', ProductCreateFormView.as_view(), name='product-form'),
    path('notes/', NoteListView.as_view(), name='notes-view'),
    path('notes/<int:pk>', NoteDetailView.as_view(), name='note-detail-view'),
    path('category/<int:category_id>/', CategoryProductFilter.as_view(), name='categories-view'),
    ]
