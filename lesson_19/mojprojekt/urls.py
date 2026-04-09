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
from ogloszenia.views import hello_world, show_product, HelloWorld2, show_ogloszenia
from blog.views import home_view, contact_view, info, rules, greet_user
from product.views import show_products, ShowProducts, AddProduct, ViewCategory
from notatnik.views import show_all_notes, show_note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('product/<int:product_id>/', show_product),
    path('hello2/', HelloWorld2.as_view()),
    path('home/', home_view, name='home-view'),
    path('contact/', contact_view),
    path('ogloszenia/', show_ogloszenia),
    path('info/', info),
    path('rules/', rules),
    path('user/<str:username>/', greet_user),
    path('show_products/', show_products),
    path('show_products2/', ShowProducts.as_view()),
    path('notes/', show_all_notes),
    path('notes/note/<int:note_id>/', show_note),
    path('add_product/', AddProduct.as_view()),
    path('category/<int:category_int>/', ViewCategory.as_view())
]
