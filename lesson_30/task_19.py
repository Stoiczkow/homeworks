# Zadanie 19 – AI: Równoległa analiza sentymentu (symulacja)

# Stwórz listę 20 przykładowych zdań (opinii o produkcie). Napisz funkcję
# analizuj_sentyment(zdanie), która symuluje zapytanie do API AI przez time.sleep(random.uniform(0.5, 2.0)) i zwraca losowo "Pozytywny", "Negatywny" lub
# "Neutralny". Użyj puli wątków (concurrent.futures.ThreadPoolExecutor), aby przeanalizować wszystkie zdania i zebrać wyniki. Zmierz czas wykonania.

import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# 20 przykładowych opinii o produkcie
opinie = [
    "Produkt działa świetnie i spełnia moje oczekiwania.",
    "Jestem bardzo niezadowolony z jakości wykonania.",
    "Neutralny produkt, nic szczególnego.",
    "Rewelacja! Kupię jeszcze raz.",
    "Nie działa tak jak w opisie.",
    "OK, ale mogło być lepiej.",
    "Bardzo dobra jakość za tę cenę.",
    "Zepsuł się po tygodniu użytkowania.",
    "Działa poprawnie, bez rewelacji.",
    "Najlepszy zakup w tym roku!",
    "Nie polecam, strata pieniędzy.",
    "Wszystko zgodne z opisem.",
    "Średni produkt, ani dobry ani zły.",
    "Jestem zachwycony funkcjonalnością.",
    "Słaba jakość materiałów.",
    "Działa, ale głośno i wolno.",
    "Bardzo solidny i dobrze wykonany.",
    "Rozczarowanie, spodziewałem się więcej.",
    "Spełnia swoje zadanie.",
    "Fantastyczny produkt, polecam każdemu!"
]

# Funkcja symulująca zapytanie do API AI
def analizuj_sentyment(zdanie):
    time.sleep(random.uniform(0.5, 2.0))  # symulacja opóźnienia
    return zdanie, random.choice(["Pozytywny", "Negatywny", "Neutralny"])


def main():
    start = time.time()

    wyniki = []

    # Pula wątków
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(analizuj_sentyment, zdanie) for zdanie in opinie]

        for future in as_completed(futures):
            wyniki.append(future.result())

    end = time.time()

    # Wyniki
    print("\nWYNIKI ANALIZY:\n")
    for zdanie, sentyment in wyniki:
        print(f"{zdanie} -> {sentyment}")

    print(f"\nCzas wykonania: {end - start:.2f} sekundy")


if __name__ == "__main__":
    main()