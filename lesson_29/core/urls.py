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

from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Zadanie 1.
    path('hello/', views.hello_world_view, name='hello'),

    #Zadanie 2.
    path('multiply/', views.multiply_view, name='multiply'),

    #Zadanie 3.
    path('save-timestamp/', views.save_timestamp_view, name='log_timestamp'),

    #Zadanie 5
    path('count-users/', views.count_users_view, name='count_users'),

    #Zadanie 7.
    path('update-last-login/<int:user_id>/', views.update_last_login_view, name='update_last_login'),

    #Zadanie 8.
      path("process-video/", views.start_video_processing, name="video"),
]
