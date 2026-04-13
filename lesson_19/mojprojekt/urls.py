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
from ogloszenia.views import hello_world, show_product, show_ogloszenia
from blog.views import home_view, contact_view, info, rules, greet_user
from product.views import show_products, ShowProducts, AddProduct, show_category
from notatnik.views import all_notes, note_detail, add_note


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/", hello_world),
    path("product/<int:product_id>/", show_product),
    path('home/', home_view, name='home-view'),
    path('contact/', contact_view),
    path("ogloszenia", show_ogloszenia),
    path("info/", info),
    path("rules", rules),
    path("user/<str:username>/", greet_user),
    path("products/", show_products, name='products'),  # Zad 7 dodanie sciezki do widoku zeby byly w products (redirect)
    path("category/<int:category_id>/", show_category, name='category'),  # Dynamiczna trasa dla kategorii
    path("products2/", ShowProducts.as_view()), # jak mamy produkt klasowy to dajemy as view
    path('notes/', all_notes, name='notes_list'), # Zad 6 lista zadan
    path('notes/add/', add_note, name='note_add'), # dodane zadania
    path('notes/<int:note_id>/', note_detail, name='note_detail'), # szczegoly zadania
    path("products/add/", AddProduct.as_view(), name='add_product'),
]



