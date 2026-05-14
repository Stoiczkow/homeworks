from django.urls import path

from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('info/', views.info_view, name='info'),
    path('rules/', views.rules_view, name='rules'),
    path('user/<str:username>/', views.user_profile_view, name='user-profile'),
    path('products/', views.product_list_view, name='product-list'),
    path('products/add/', views.product_create_view, name='product-add'),
    path('category/<int:category_id>/', views.category_products_view, name='category-products'),
    path('notes/', views.note_list_view, name='note-list'),
    path('note/<int:note_id>/', views.note_detail_view, name='note-detail'),
]