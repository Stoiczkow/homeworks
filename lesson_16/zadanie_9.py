# Zasob na serwerze pod adresem /users/1:
# {"name": "Katarzyna", "email": "k.nowak@example.com", "city": "Warszawa"}

# PUT - zastepuje caly zasob. Nawet jesli chcemy zmienic tylko imie,
# musimy wyslac WSZYSTKIE pola. Pola pominiete zostana usuniete lub zastapione nullem.
zadanie_put = {
    "method": "PUT",
    "target": "/users/1",
    "body": {
        "name": "Kasia",
        "email": "k.nowak@example.com",
        "city": "Warszawa"
    }
}

# PATCH - modyfikuje tylko podane pola. Wysylamy wylacznie to, co chcemy zmienic.
# Jest bardziej "oszczedny" - przesylamy mniej danych, a pozostale pola pozostaja bez zmian.
zadanie_patch = {
    "method": "PATCH",
    "target": "/users/1",
    "body": {
        "name": "Kasia"
    }
}

print("PUT body:", zadanie_put["body"])
print("PATCH body:", zadanie_patch["body"])

# PATCH jest bardziej oszczedny - przesyla tylko zmieniane pole,
# PUT wymaga przeslania kompletnej reprezentacji zasobu.
