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
from products import views
# from products.views import home
from django.contrib.auth import views as autoViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', autoViews.LoginView.as_view
         (template_name='users/login.html'), name='login'),
    path('logout/', autoViews.LogoutView.as_view
        (template_name='users/logout.html'), name='logout'),
    path('home/', views.home, name='home'), 
    path('change_password/', autoViews.PasswordChangeView.as_view
         (template_name='users/password_change_form.html'), name = 'password_change'),
    path('change_password_done/', autoViews.PasswordChangeDoneView.as_view
        (template_name='users/password_change_done.html'), name = 'password_change_done'),
    path('users_list/', views.users_list, name='users_list')
]

 