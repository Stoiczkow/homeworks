from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Zadanie 8 – chroniony endpoint dostępny tylko dla zalogowanych użytkowników.
# Bez tokenu → 401 Unauthorized
# Z nagłówkiem Authorization: Bearer <access_token> → 200 + nazwa użytkownika
class ProfilView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'message': f'Witaj, {request.user.username}!',
            'username': request.user.username,
            'email': request.user.email,
        })


# Zadanie 5 – rejestracja użytkownika przez Postman:
# POST /auth/users/
# Body (JSON): { "username": "testuser", "password": "Haslo1234!", "re_password": "Haslo1234!" }
# Odpowiedź: 201 Created z danymi nowego użytkownika.
# Weryfikacja: panel admina /admin/ → Users.

# Zadanie 6 – logowanie i inspekcja tokenu:
# POST /auth/jwt/create/
# Body (JSON): { "username": "testuser", "password": "Haslo1234!" }
# Odpowiedź: { "access": "eyJ...", "refresh": "eyJ..." }
# Po wklejeniu access tokenu na jwt.io w sekcji Payload widoczne są:
#   "user_id": <id użytkownika>
#   "exp": <timestamp Unix – czas wygaśnięcia>
#   "iat": <timestamp Unix – czas wystawienia>
#   "jti": <unikalny identyfikator tokenu>

# Zadanie 9 – czas życia tokenu = 10 sekund (skonfigurowane w settings.py):
# Po zalogowaniu → użycie tokenu w ciągu 10 sekund → 200 OK
# Po odczekaniu 10 sekund → 401 Unauthorized:
# { "detail": "Given token not valid for any token type",
#   "code": "token_not_valid",
#   "messages": [{"token_class": "AccessToken", "token_type": "access",
#                 "message": "Token is invalid or expired"}] }

# Zadanie 10 – odświeżanie tokenu:
# POST /auth/jwt/refresh/
# Body (JSON): { "refresh": "<twój_refresh_token>" }
# Odpowiedź: { "access": "eyJ..." }  ← nowy, świeży access token
# Nowy token można użyć do odpytania GET /api/profil/ z nagłówkiem:
# Authorization: Bearer <nowy_access_token>  → 200 OK
