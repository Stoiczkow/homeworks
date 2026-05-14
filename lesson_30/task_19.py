# Zadanie 19 – AI: Równoległa analiza sentymentu (symulacja)
# Stwórz listę 20 przykładowych zdań (opinii o produkcie). Napisz funkcję
# analizuj_sentyment(zdanie), która symuluje zapytanie do API AI przez
# time.sleep(random.uniform(0.5, 2.0)) i zwraca losowo "Pozytywny", "Negatywny" lub
# "Neutralny". Użyj puli wątków (concurrent.futures.ThreadPoolExecutor), aby przeanalizować
# wszystkie zdania i zebrać wyniki. Zmierz czas wykonania.

import concurrent.futures
import random
import time


opinie = [
	"Ten produkt jest świetny i bardzo przydatny.",
	"Jakość wykonania jest naprawdę dobra.",
	"Nie jestem zadowolony z tego zakupu.",
	"Produkt działa zgodnie z opisem.",
	"Obsługa była bardzo miła i pomocna.",
	"Towar przyszedł uszkodzony.",
	"Cena jest adekwatna do jakości.",
	"Bateria rozładowuje się zbyt szybko.",
	"Wygląda lepiej niż na zdjęciach.",
	"Instrukcja obsługi jest nieczytelna.",
	"Dostawa była szybka i bez problemów.",
	"Nie polecam tego produktu nikomu.",
	"Spełnia moje oczekiwania.",
	"Kolor różni się od tego na stronie.",
	"Używam go codziennie i jestem zadowolony.",
	"Produkt jest przeciętny, nic specjalnego.",
	"Materiał wydaje się tani.",
	"Bardzo łatwy w użyciu.",
	"Mam mieszane uczucia co do tego zakupu.",
	"Z pewnością kupię ten produkt ponownie.",
]


def analizuj_sentyment(zdanie):
	time.sleep(random.uniform(0.5, 2.0))
	return random.choice(["Pozytywny", "Negatywny", "Neutralny"])


def main():
	start = time.perf_counter()

	with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
		wyniki = list(executor.map(analizuj_sentyment, opinie))

	koniec = time.perf_counter()

	print("Wyniki analizy sentymentu:\n")
	for numer, (zdanie, wynik) in enumerate(zip(opinie, wyniki), start=1):
		print(f"{numer}. {zdanie}")
		print(f"   Sentyment: {wynik}")

	print(f"\nCzas wykonania: {koniec - start:.2f} sekundy")


if __name__ == "__main__":
	main()

