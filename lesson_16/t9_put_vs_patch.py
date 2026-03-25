"""
9.
PUT vs PATCH: Wyobraź sobie, że na serwerze pod adresem /users/1 znajduje się
następujący zasób w formacie JSON: {"name": "Katarzyna", "email":
"k.nowak@example.com", "city": "Warszawa"} .
Opisz, jak wyglądałoby ciało żądania PUT , aby zmienić tylko imię na "Kasia".
Opisz, jak wyglądałoby ciało żądania PATCH , aby zmienić tylko imię na "Kasia".
Wyjaśnij w komentarzu w kodzie, dlaczego te żądania się różnią i która metoda jest
bardziej "oszczędna" pod względem przesyłanych danych.
"""

current_user = {
    "name": "Katarzyna",
    "email": "k.nowak@example.com",
    "city": "Warszawa",
}

# PUT nadpisuje caly zasob, wiec trzeba wyslac komplet danych (takze tych bez zmian).
put_body = {
    "name": "Kasia",
    "email": "k.nowak@example.com",
    "city": "Warszawa",
}

# PATCH aktualizuje tylko wskazane pola, wiec wysylamy tylko zmienione dane.
patch_body = {
    "name": "Kasia",
}

print("Obecny zasob:")
print(current_user)
print("\nPrzyklad ciala PUT:")
print(put_body)
print("\nPrzyklad ciala PATCH:")
print(patch_body)
print("\nPATCH jest bardziej oszczedny, bo przesyla mniej danych.")
