# Zadanie 15 – Prosty web crawler
# Napisz prosty crawler, który zaczyna od jednego adresu URL. Pobiera jego zawartość,
# znajduje w niej wszystkie linki do tej samej domeny, a następnie dodaje je do kolejki do
# odwiedzenia. Użyj puli wątków do jednoczesnego pobierania stron z kolejki. Ogranicz liczbę
# odwiedzonych stron do np. 50, aby nie "zalać" serwera. Użyj bezpiecznej wątkowo kolejki i
# zbioru (set) do przechowywania już odwiedzonych linków.

import requests
from bs4 import BeautifulSoup
from threading import Thread, Lock
from queue import Queue


session = requests.Session()
session.headers.update({"User-agent": "WebAgent/1.0"})

DOMAIN = "onet.pl"

full_root_url = "https://" + DOMAIN

root_file = session.get(full_root_url).text

parsed_root = BeautifulSoup(root_file, features="lxml")

a_selectors = parsed_root.find_all('a')

hrefs = []

for a in a_selectors:
    href = a.get('href')
    
    if href and DOMAIN in href:
        hrefs.append(href)

trimmed_hrefs = hrefs[:50]

def crawl(href_queue, visited_urls, lock):
    while not href_queue.empty():
        url = href_queue.get()
        print(f"Łączę się z {url}")
        response = session.get(url).text
        with lock:
            visited_urls.add(url)

if __name__ == "__main__":
    visited_urls = set()

    lock = Lock()
    q = Queue()

    for href in trimmed_hrefs:
        q.put(href)

    threads = []

    for t in range(2):
        thread = Thread(target=crawl, args=(q, visited_urls, lock))
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

    print(visited_urls)