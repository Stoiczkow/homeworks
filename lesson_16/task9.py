#PUT vs PATCH: Wyobraź sobie, że na serwerze pod adresem /users/1 znajduje się następujący zasób w formacie JSON: {"name": "Katarzyna", "email": "k.nowak@example.com", "city": "Warszawa"} 

# Opisz, jak wyglądałoby ciało żądania PUT , aby zmienić tylko imię na "Kasia".

{
  "name": "Katarzyna",
  "email": "k.nowak@example.com",
  "city": "Warszawa"
}
#PUT /user
put_data = {
    "name": "Kasia",
    "email": "k.nowak@example.com",
    "city": "Warszawa"
}

# Opisz, jak wyglądałoby ciało żądania PATCH , aby zmienić tylko imię na "Kasia"

patch_body = {
    "name": "Kasia"
}

# Wyjaśnij w komentarzu w kodzie, dlaczego te żądania się różnią i która metoda jest bardziej "oszczędna" pod względem przesyłanych danych

#PATCH jest bardziej oszczędny bo przesyła mniej danych do serwera (tylko zmiany)