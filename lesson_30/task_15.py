# Napisz prosty crawler, który zaczyna od jednego adresu URL. Pobiera jego zawartość,
# znajduje w niej wszystkie linki do tej samej domeny, a następnie dodaje je do kolejki do
# odwiedzenia. Użyj puli wątków do jednoczesnego pobierania stron z kolejki. Ogranicz liczbę
# odwiedzonych stron do np. 50, aby nie "zalać" serwera. Użyj bezpiecznej wątkowo kolejki i
# zbioru (set) do przechowywania już odwiedzonych linków

import re
import requests

from queue import Queue
from threading import Lock
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse


MAX_PAGES = 50
NUM_WORKERS = 5

start_url = "https://example.com"
domain = urlparse(start_url).netloc

visited = set()
visited_lock = Lock()

url_queue = Queue()
url_queue.put(start_url)


def extract_links(html):
    return re.findall(
        r'href=["\']([^"\']+)["\']',
        html
    )


def crawl():
    while True:

        try:
            url = url_queue.get(timeout=1)
        except:
            return

        try:
            response = requests.get(url, timeout=5)

            print("Odwiedzam:", url)

            links = extract_links(response.text)

            for link in links:
                full_url = urljoin(url, link)

                parsed = urlparse(full_url)

                if parsed.netloc != domain:
                    continue

                with visited_lock:

                    if len(visited) >= MAX_PAGES:
                        continue

                    if full_url not in visited:
                        visited.add(full_url)
                        url_queue.put(full_url)

        except Exception as e:
            print(f"Błąd dla {url}: {e}")

        finally:
            url_queue.task_done()


with visited_lock:
    visited.add(start_url)

with ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
    for _ in range(NUM_WORKERS):
        executor.submit(crawl)

url_queue.join()

print(f"\nOdwiedzono {len(visited)} stron:")
for url in visited:
    print(url)