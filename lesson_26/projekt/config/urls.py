from django.contrib import admin
from django.urls import path, include

# Zadanie 4 – ścieżki djoser dla rejestracji/zarządzania użytkownikami
# oraz simplejwt dla tworzenia i odświeżania tokenów JWT
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/', include('api.urls')),
]

# Dostępne endpointy po konfiguracji:
# POST /auth/users/                  – rejestracja (zadanie 5)
# POST /auth/jwt/create/             – logowanie → access + refresh token (zadanie 6)
# POST /auth/jwt/refresh/            – odświeżenie access tokenu (zadanie 10)
# GET  /api/profil/                  – chroniony endpoint (zadanie 8)
