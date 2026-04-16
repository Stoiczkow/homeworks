# PUT vs PATCH: Wyobraź sobie, że na serwerze pod adresem /users/1 znajduje się
# następujący zasób w formacie JSON: {"name": "Katarzyna", "email":
# "k.nowak@example.com", "city": "Warszawa"} .
# Opisz, jak wyglądałoby ciało żądania PUT , aby zmienić tylko imię na "Kasia".
# Opisz, jak wyglądałoby ciało żądania PATCH , aby zmienić tylko imię na "Kasia".
# Wyjaśnij w komentarzu w kodzie, dlaczego te żądania się różnią i która metoda jest bardziej "oszczędna" pod względem przesyłanych danych.

put_body = {
    "name": "Kasia",
    "email": "k.nowak@example.com",
     "city": "Warszawa"
}

patch_body = {
    "name": "Kasia"
}




# Put to po prostu wysyłanie całego obiektu na nowo zastępując poprzedni, a patch wysyła tylko zmienione pole, co logiczne w przypadku zmiany jednego pola patch jest bardziej oszczędny.