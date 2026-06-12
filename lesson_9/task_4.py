"""
Odczyt konfiguracji:
Program odczytuje plik config.json i wyświetla komunikat:
"Witaj, [uzytkownik]! Twój motyw to [motyw]."
"""

import json

with open("config.json", "r", encoding="utf-8") as f:
    dane = json.load(f)

print(f"Witaj, {dane['uzytkownik']}! Twój motyw to {dane['motyw']}.")
