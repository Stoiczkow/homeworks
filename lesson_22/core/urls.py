from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Zadanie 10 – allauth (rejestracja, logowanie, wylogowanie)
    path('accounts/', include('allauth.urls')),
    path('', include('blog.urls')),
]
