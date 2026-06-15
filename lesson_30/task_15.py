import threading
import queue
from html.parser import HTMLParser
from urllib.request import Request, urlopen
from urllib.parse import urljoin, urlparse


START_URL = "https://docs.python.org/3/"
MAX_PAGES = 50
WORKERS = 5


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr_name, attr_value in attrs:
                if attr_name == "href":
                    self.links.append(attr_value)


def is_same_domain(url, start_domain):
    parsed_url = urlparse(url)
    return parsed_url.netloc == start_domain


def normalize_url(link, base_url):
    full_url = urljoin(base_url, link)
    parsed = urlparse(full_url)

    clean_url = parsed._replace(fragment="").geturl()

    return clean_url


def fetch_html(url):
    request = Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urlopen(request, timeout=5) as response:
        content_type = response.headers.get("Content-Type", "")

        if "text/html" not in content_type:
            return ""

        return response.read().decode("utf-8", errors="ignore")


def extract_links(html):
    parser = LinkParser()
    parser.feed(html)
    return parser.links


def worker(to_visit, visited, seen, lock, start_domain):
    while True:
        url = to_visit.get()

        if url is None:
            to_visit.task_done()
            break

        with lock:
            if url in visited:
                to_visit.task_done()
                continue

            if len(visited) >= MAX_PAGES:
                to_visit.task_done()
                continue

            visited.add(url)

        print(f"Pobieram: {url}")

        try:
            html = fetch_html(url)
            links = extract_links(html)
        except Exception as error:
            print(f"Błąd przy {url}: {error}")
            to_visit.task_done()
            continue

        for link in links:
            new_url = normalize_url(link, url)

            if not is_same_domain(new_url, start_domain):
                continue

            with lock:
                if len(seen) >= MAX_PAGES:
                    break

                if new_url not in seen:
                    seen.add(new_url)
                    to_visit.put(new_url)

        to_visit.task_done()


if __name__ == "__main__":
    start_domain = urlparse(START_URL).netloc

    to_visit = queue.Queue()
    visited = set()
    seen = set()
    lock = threading.Lock()

    to_visit.put(START_URL)
    seen.add(START_URL)

    threads = []

    for _ in range(WORKERS):
        thread = threading.Thread(
            target=worker,
            args=(to_visit, visited, seen, lock, start_domain)
        )
        threads.append(thread)
        thread.start()

    to_visit.join()

    for _ in range(WORKERS):
        to_visit.put(None)

    for thread in threads:
        thread.join()

    print("-" * 40)
    print(f"Odwiedzone strony: {len(visited)}")

    for url in visited:
        print(url)