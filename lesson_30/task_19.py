import time, random
from concurrent.futures import ThreadPoolExecutor

# Zadanie 19 – AI: Równoległa analiza sentymentu (symulacja)
# Stwórz listę 20 przykładowych zdań (opinii o produkcie). Napisz funkcję
# analizuj_sentyment(zdanie), która symuluje zapytanie do API AI przez
# time.sleep(random.uniform(0.5, 2.0)) i zwraca losowo "Pozytywny", "Negatywny" lub
# "Neutralny". Użyj puli wątków (concurrent.futures.ThreadPoolExecutor), aby przeanalizować
# wszystkie zdania i zebrać wyniki. Zmierz czas wykonania.

sentences = [
    "Jestem bardzo zadowolony z jakości dźwięku, która przewyższyła moje oczekiwania.",
    "Bateria wytrzymuje naprawdę długo, nawet przy intensywnym użytkowaniu.",
    "Słuchawki są wygodne i nie powodują dyskomfortu podczas długiego noszenia.",
    "Połączenie Bluetooth działa stabilnie i nie zrywa sygnału.",
    "Stosunek jakości do ceny jest bardzo dobry.",
    "Mikrofon sprawdza się dobrze podczas rozmów telefonicznych.",
    "Design produktu jest nowoczesny i estetyczny.",
    "Obsługa dotykowa działa płynnie i intuicyjnie.",
    "Dźwięk jest czysty, a basy dobrze słyszalne.",
    "Produkt spełnił wszystkie moje oczekiwania.",
    "Czasami zdarzają się drobne opóźnienia przy oglądaniu filmów.",
    "Etui ładujące jest kompaktowe i wygodne do przenoszenia.",
    "Jakość wykonania sprawia wrażenie solidnej i trwałej.",
    "Słuchawki dobrze tłumią hałas z otoczenia.",
    "Proces parowania z telefonem był bardzo prosty.",
    "Po kilku tygodniach użytkowania nadal działają bez zarzutu.",
    "Przy maksymalnej głośności dźwięk pozostaje wyraźny.",
    "Instrukcja obsługi mogłaby być nieco bardziej szczegółowa.",
    "To jeden z lepszych produktów w tej kategorii cenowej.",
    "Zdecydowanie poleciłbym ten produkt znajomym."
]

def analize_sentence(sentence):
    time.sleep(random.uniform(0.5, 2.0))
    
    return random.choice(["Pozytywny", "Negatywny", "Neutralny"])

start = time.time()

with ThreadPoolExecutor(max_workers=20) as executor:
    results = list(executor.map(analize_sentence, sentences))
    
end = time.time()

for result, sentence in zip(results, sentences):
    print(f"{result:10} | {sentence}")
    
print(f"Czas wykonania: {end - start:.2f} s")