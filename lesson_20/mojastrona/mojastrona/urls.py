from django.contrib import admin
from django.urls import path, include
from sklep import views as sklep_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', sklep_views.info_view, name='info'),
    path('rules/', sklep_views.rules_view, name='rules'),
    path('user/<str:username>/', sklep_views.user_profile, name='user-profile'),
    path('products/', sklep_views.product_list, name='product-list'),
    path('products/add/', sklep_views.product_create, name='product-create'),
    path('category/<int:category_id>/', sklep_views.category_products, name='category-products'),
    path('notes/', include('notatnik.urls')),
]
