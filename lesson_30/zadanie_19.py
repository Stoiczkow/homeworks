import random
import time
from concurrent.futures import ThreadPoolExecutor

SENTIMENTS = ("Pozytywny", "Negatywny", "Neutralny")

REVIEWS = [
    "Świetny produkt, polecam każdemu!",
    "Zdecydowanie nie warto wydawać tych pieniędzy.",
    "Jest okej, nic specjalnego.",
    "Najlepszy zakup w tym roku.",
    "Bardzo szybko się zepsuł.",
    "Cena adekwatna do jakości.",
    "Przeciętny, oczekiwałem więcej.",
    "Zachwycona, dziękuję!",
    "Słaba obsługa klienta.",
    "Solidnie wykonany, jestem zadowolony.",
    "Nie spełnił moich oczekiwań.",
    "Idealny prezent dla bliskiej osoby.",
    "Pakowanie pozostawia wiele do życzenia.",
    "Bardzo dobry stosunek ceny do jakości.",
    "Niestety, otrzymałem uszkodzony egzemplarz.",
    "Działa zgodnie z opisem.",
    "Mogłoby być lepsze.",
    "Super, kupuję drugi raz.",
    "Strata pieniędzy.",
    "Polecam ze wskazaniem.",
]


def analyze_sentiment(sentence: str) -> tuple[str, str]:
    time.sleep(random.uniform(0.5, 2.0))
    return sentence, random.choice(SENTIMENTS)


if __name__ == "__main__":
    random.seed(7)

    start = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(analyze_sentiment, REVIEWS))
    elapsed = time.time() - start

    for sentence, sentiment in results:
        print(f"[{sentiment}] {sentence}")

    print(f"\nPrzetworzono {len(results)} opinii w {elapsed:.2f} s")