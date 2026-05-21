# 9. PUT vs PATCH: Wyobraź sobie, że na serwerze pod adresem /users/1 znajduje się
# następujący zasób w formacie JSON: {"name": "Katarzyna", "email":
# "k.nowak@example.com", "city": "Warszawa"} .
# Opisz, jak wyglądałoby ciało żądania PUT , aby zmienić tylko imię na "Kasia".
# Opisz, jak wyglądałoby ciało żądania PATCH , aby zmienić tylko imię na "Kasia".
# Wyjaśnij w komentarzu w kodzie, dlaczego te żądania się różnią i która metoda jest
# bardziej "oszczędna" pod względem przesyłanych danych.

request_put = {
    "method": "PUT",
    "target": "/users/1",
    "body": {"name": "Kasia", 
             "email": "k.nowak@example.com", 
             "city": "Warszawa"}
}

request_patch = {
    "method": "PATCH",
    "target": "/users/1",
    "body": {"name": "Kasia"}
}

# w ciele żądania PUT podajemy cały zasób (nawet te pola, które się nie zmieniają), a w ciele żąðania PATCH podajemy tylko te pola, których wartości chcemy zmienić. Dlatego bardziej oszczędna będzie metoda PATCH, ponieważ wysyłamy mniejsze ilości danych