"""
Konfiguracja w JSON:
Stwórz słownik ustawień aplikacji i zapisz go do pliku config.json
z wcięciami i poprawnym kodowaniem polskich znaków.
"""

import json

konfiguracja = {
    "uzytkownik": "admin",
    "motyw": "ciemny",
    "rozdzielczosc": [1920, 1080]
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(konfiguracja, f, ensure_ascii=False, indent=4)
