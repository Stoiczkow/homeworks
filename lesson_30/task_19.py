import concurrent.futures
import random
import time


opinions = [
    "Produkt jest bardzo dobry.",
    "Nie jestem zadowolony z zakupu.",
    "Dostawa była szybka.",
    "Jakość wykonania jest słaba.",
    "Cena jest rozsądna.",
    "Obsługa klienta była pomocna.",
    "Nie kupiłbym tego ponownie.",
    "Produkt spełnił moje oczekiwania.",
    "Opakowanie było uszkodzone.",
    "Wszystko działa poprawnie.",
    "Mam mieszane uczucia.",
    "Produkt wygląda lepiej niż na zdjęciach.",
    "Bateria rozładowuje się zbyt szybko.",
    "Instrukcja była czytelna.",
    "Aplikacja czasami się zacina.",
    "Polecam ten produkt.",
    "Nie polecam tego nikomu.",
    "Jest okej, ale bez rewelacji.",
    "Dobra jakość za tę cenę.",
    "Produkt przyszedł za późno.",
]


def analizuj_sentyment(zdanie):
    time.sleep(random.uniform(0.5, 2.0))

    sentyment = random.choice(["Pozytywny", "Negatywny", "Neutralny"])

    return zdanie, sentyment


if __name__ == "__main__":
    start = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(analizuj_sentyment, opinions))

    end = time.time()

    for opinion, sentiment in results:
        print(f"Opinia: {opinion}")
        print(f"Sentyment: {sentiment}")
        print("-" * 40)

    print(f"Czas wykonania: {end - start:.2f} sekund")