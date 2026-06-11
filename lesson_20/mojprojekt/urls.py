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

from info.views import info_view
from notatnik.views import ListaNotatekView, NoteDetailView
from product.views import ProductView
from user.views import user_view
from rules.views import rules_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # task_1 - start
    path('info/', info_view, name="info"),
    path('rules/', rules_view, name="rules"),

    # task_2
    path('user/<str:username>/', user_view, name='user'),

    #task_4 i task_5
    path('product/', ProductView.as_view(), name="product"),

    #task_6
    path('notatnik/', ListaNotatekView.as_view(), name='notatki'),
    path('notatnik/<int:notatka_id>/', NoteDetailView.as_view(), name='notatka')
]
