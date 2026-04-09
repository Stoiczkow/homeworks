"""
URL configuration for mojprojekt project.

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
from ogloszenia.views import hello_world, show_product, hello_world2, show_ogloszenia
from blog.views import home_view, contact_view
from ogloszenia.views import info_view, rules_view, hello_username_view
from notatnik.views import show_notes, show_note_details

from product.views import show_products, ShowProduct, AddProduct, show_products_from_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('product/<int:product_id>/', show_product, name='product-details'),
    path('home', home_view, name='home-view'),
    path('contact/', contact_view, name='contact-view'),
    path('ogloszenia/', show_ogloszenia),
    path('info/', info_view),
    path('rules/', rules_view),
    path('user/<str:username>/', hello_username_view, name='username-hello'),
    path('products/', show_products),
    path('products2/', ShowProduct.as_view(), name='products-view'),
    path('products/add/', AddProduct.as_view()),
    path('notes/', show_notes),
    path('note/<int:note_id>/', show_note_details, name='note-details'),
    path('category/<int:category_id>/', show_products_from_category, name='products-from-category')
]
