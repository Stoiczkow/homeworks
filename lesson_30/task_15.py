# Zadanie 15 – Prosty web crawler

# Napisz prosty crawler, który zaczyna od jednego adresu URL. Pobiera jego zawartość,
# znajduje w niej wszystkie linki do tej samej domeny, a następnie dodaje je do kolejki  odwiedzenia. Użyj puli wątków do jednoczesnego pobierania stron z kolejki. Ogranicz liczbę odwiedzonych stron do np. 50, aby nie "zalać" serwera. Użyj bezpiecznej wątkowo kolejki i zbioru (set) do przechowywania już odwiedzonych linków.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from queue import Empty, Queue
from concurrent.futures import ThreadPoolExecutor
import threading

MAX_PAGES = 50
NUM_THREADS = 10

start_url = "https://wp.pl"

url_queue = Queue()
url_queue.put(start_url)

visited = set()
lock = threading.Lock()


def is_same_domain(url1, url2):
    return urlparse(url1).netloc == urlparse(url2).netloc


def crawl():
    while True:
        try:
            url = url_queue.get(timeout=3)
        except Empty:
            return

        with lock:
            if len(visited) >= MAX_PAGES:
                url_queue.task_done()
                return
            if url in visited:
                url_queue.task_done()
                continue
            visited.add(url)

        try:
            print(f"[+] Pobieram: {url}")
            response = requests.get(url, timeout=5)
            if "text/html" not in response.headers.get("Content-Type", ""):
                url_queue.task_done()
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link["href"])

                with lock:
                    if len(visited) >= MAX_PAGES:
                        break

                if is_same_domain(start_url, full_url):
                    url_queue.put(full_url)

        except Exception as e:
            print(f"[!] Błąd {url}: {e}")

        url_queue.task_done()


def main():
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        for _ in range(NUM_THREADS):
            executor.submit(crawl)

    url_queue.join()

    print("\n=== Zakończono ===")
    print(f"Odwiedzone strony: {len(visited)}")


if __name__ == "__main__":
    main()