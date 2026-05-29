"""
Zadanie 19 – Równoległa analiza sentymentu (symulacja)
ThreadPoolExecutor analizuje 20 zdań jednocześnie, symulując opóźnienie API.
"""
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

ZDANIA = [
    "Ten produkt jest absolutnie fantastyczny!",
    "Jakość pozostawia wiele do życzenia.",
    "Dostawa była na czas, produkt spełnił oczekiwania.",
    "Nigdy więcej nie kupię czegoś od tej firmy.",
    "Jestem zachwycony obsługą klienta.",
    "Produkt przyszedł uszkodzony.",
    "Cena jest przystępna jak na taką jakość.",
    "Nic specjalnego, ale też nic złego.",
    "Polecam wszystkim znajomym!",
    "Rozczarowanie – opis nie odpowiada rzeczywistości.",
    "Solidny produkt, działa bez zarzutu.",
    "Opakowanie było zniszczone przy dostawie.",
    "Bardzo dobra relacja jakości do ceny.",
    "Produkt jest dokładnie taki, jak w opisie.",
    "Obsługa klienta była pomocna i szybka.",
    "Materiał jest słabej jakości.",
    "Zamówię jeszcze raz – jestem zadowolony.",
    "Produkt spełnił moje podstawowe oczekiwania.",
    "Zdecydowanie warto kupić!",
    "Nie polecam, dużo lepsze alternatywy na rynku.",
]


def analizuj_sentyment(zdanie):
    time.sleep(random.uniform(0.5, 2.0))
    wynik = random.choice(['Pozytywny', 'Negatywny', 'Neutralny'])
    return zdanie, wynik


if __name__ == '__main__':
    start = time.perf_counter()

    wyniki = {}
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(analizuj_sentyment, z): z for z in ZDANIA}
        for future in as_completed(futures):
            zdanie, sentyment = future.result()
            wyniki[zdanie] = sentyment
            print(f"[{sentyment:9}] {zdanie[:60]}")

    czas = time.perf_counter() - start
    print(f"\nCzas analizy {len(ZDANIA)} zdań: {czas:.2f}s")

    for s in ['Pozytywny', 'Negatywny', 'Neutralny']:
        count = sum(1 for v in wyniki.values() if v == s)
        print(f"  {s}: {count}")
