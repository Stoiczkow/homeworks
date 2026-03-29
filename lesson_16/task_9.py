# Zasób na serwerze pod /users/1
current_resource = {
    "name": "Katarzyna",
    "email": "k.nowak@example.com",
    "city": "Warszawa"
}


"""
PUT oznacza "zastąp zasób pod tym adresem tym, co wysyłam".
Serwer usuwa stary obiekt i zapisuje dokładnie to, co przyszło w żądaniu.
Jeśli pominiesz pole (np. "city"), serwer potraktuje to jako jego usunięcie.
Musisz więc wysłać WSZYSTKIE pola - nawet te, których nie zmieniasz.
"""

put_request = {
    "method": "PUT",
    "target": "/users/1",
    "body": {
        "name": "Kasia",                  # zmienione
        "email": "k.nowak@example.com",   # bez zmian
        "city": "Warszawa"                # bez zmian
    }
}


"""
PATCH oznacza "zaktualizuj tylko te pola, które wysyłam, reszty nie ruszaj".
Serwer scala (merge) przychodzące dane z istniejącym zasobem.
Pominiete pola pozostają niezmienione - nie są usuwane.
Wysyłasz tylko to, co faktycznie chcesz zmienić.
"""

patch_request = {
    "method": "PATCH",
    "target": "/users/1",
    "body": {
        "name": "Kasia"   # tylko zmieniane pole
    }
}


put_size   = len(str(put_request["body"]))
patch_size = len(str(patch_request["body"]))

print("=== PUT body ===")
print(put_request["body"])
print(f"Rozmiar: ~{put_size} znaków\n")

print("=== PATCH body ===")
print(patch_request["body"])
print(f"Rozmiar: ~{patch_size} znaków\n")

print("=== Porównanie ===")
print(f"PATCH wysyla o {put_size - patch_size} znaków mniej")
print(f"PATCH jest {put_size // patch_size}x bardziej oszczędny w tym przypadku")


"""
WNIOSKI

PATCH jest bardziej "oszczędny" - przesyła tylko zmienione dane.
Różnica rośnie wraz z rozmiarem obiektu: przy zasobie z 50 polami
PATCH wyśle 1 pole, PUT musi wysłać wszystkie 50.

Kiedy używać PUT?
   - gdy chcesz świadomie "wyczyścić" pominięte pola
   - gdy zastępujesz zasób całkowicie nową wersją

Kiedy używać PATCH?
   - gdy aktualizujesz jedno lub kilka pól
   - gdy zależy Ci na wydajności (mniej danych w sieci)
"""
