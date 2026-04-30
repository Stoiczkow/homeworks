"""
URL configuration for project project.

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
from product.views import info_, rules_, user_, show_product, createProduct, product_list,category
from notatnik.views import show_Note, show_One_Note, paginacja


urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', info_), #task1
    path('rules/', rules_), #task1
    path('user/<str:user_name>/', user_), #task2
    path('product/', show_product), #task 4
    path('notes/', show_Note), #task6
    path('note/<int:note_id>/', show_One_Note), #task6
    path('add/', createProduct, name="createProduct"),#task7
    path('show_all/',product_list, name='product_list'),#task7
    path('category/<int:category_id>/', category), #task9
    path('paginacja', paginacja, name='paginacja')#task10
]
