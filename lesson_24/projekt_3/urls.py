"""
URL configuration for projekt_3 project.

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
from django.views.generic import RedirectView
from products.views import register, profile, all_products, show_users
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(url="profile/", permanent=True)),

    path('register/', register, name='register'),
    path('login/', 
    auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', 
    auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('products/', all_products, name='products'),
    path('change-password', auth_views.PasswordChangeView.as_view(template_name='users/change_password.html'), name='changepassword'),
    path('change-password-done', auth_views.PasswordChangeDoneView.as_view(template_name='users/change_password_done.html'), name='password_change_done'),

    path('users/', show_users, name='users'),
]
