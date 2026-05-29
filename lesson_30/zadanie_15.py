"""
Zadanie 15 – Prosty web crawler
Pula wątków (ThreadPoolExecutor) pobiera strony równolegle.
Limit: 50 stron, tylko linki z tej samej domeny.
"""
import queue
import threading
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

START_URL = 'https://example.com'
MAX_PAGES = 50
WORKERS = 5

odwiedzone = set()
odwiedzone_lock = threading.Lock()
kolejka = queue.Queue()
kolejka.put(START_URL)


def pobierz_strone(url):
    try:
        response = requests.get(url, timeout=5)
        if 'text/html' not in response.headers.get('Content-Type', ''):
            return []
        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"  Pobrano: {url}")
        domena = urlparse(START_URL).netloc
        linki = []
        for a in soup.find_all('a', href=True):
            pelny_url = urljoin(url, a['href'])
            if urlparse(pelny_url).netloc == domena:
                linki.append(pelny_url)
        return linki
    except Exception as e:
        print(f"  Błąd przy {url}: {e}")
        return []


def worker():
    while True:
        try:
            url = kolejka.get(timeout=3)
        except queue.Empty:
            break

        with odwiedzone_lock:
            if url in odwiedzone or len(odwiedzone) >= MAX_PAGES:
                kolejka.task_done()
                continue
            odwiedzone.add(url)

        linki = pobierz_strone(url)
        for link in linki:
            with odwiedzone_lock:
                if link not in odwiedzone and len(odwiedzone) < MAX_PAGES:
                    kolejka.put(link)

        kolejka.task_done()


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        futures = [executor.submit(worker) for _ in range(WORKERS)]

    print(f"\nCrawler zakończony. Odwiedzono {len(odwiedzone)} stron.")
