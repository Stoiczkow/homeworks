import queue
import threading
from html.parser import HTMLParser
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen

START_URL = "https://docs.python.org/3/"
MAX_PAGES = 50
WORKER_COUNT = 5
TIMEOUT_S = 5


class LinkExtractor(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for name, value in attrs:
            if name == "href" and value:
                absolute, _ = urldefrag(urljoin(self.base_url, value))
                self.links.append(absolute)


def download(url: str) -> str | None:
    request = Request(url, headers={"User-Agent": "lesson-30-crawler"})
    try:
        with urlopen(request, timeout=TIMEOUT_S) as response:
            content_type = response.headers.get("Content-Type", "")
            if "text/html" not in content_type:
                return None
            return response.read().decode("utf-8", errors="ignore")
    except Exception as exc:
        print(f"Błąd pobierania {url}: {exc}")
        return None


def crawl(
    to_visit: queue.Queue,
    visited: set[str],
    visited_lock: threading.Lock,
    domain: str,
) -> None:
    while True:
        try:
            url = to_visit.get(timeout=2)
        except queue.Empty:
            return

        with visited_lock:
            if len(visited) >= MAX_PAGES or url in visited:
                to_visit.task_done()
                continue
            visited.add(url)

        print(f"[{threading.current_thread().name}] Pobieram: {url}")
        html = download(url)
        if html:
            parser = LinkExtractor(url)
            try:
                parser.feed(html)
            except Exception as exc:
                print(f"Błąd parsowania {url}: {exc}")
            else:
                for link in parser.links:
                    if urlparse(link).netloc == domain:
                        with visited_lock:
                            if link not in visited and len(visited) < MAX_PAGES:
                                to_visit.put(link)

        to_visit.task_done()


if __name__ == "__main__":
    domain = urlparse(START_URL).netloc
    to_visit: queue.Queue = queue.Queue()
    to_visit.put(START_URL)
    visited: set[str] = set()
    visited_lock = threading.Lock()

    workers = [
        threading.Thread(
            target=crawl,
            args=(to_visit, visited, visited_lock, domain),
            name=f"Crawler-{i + 1}",
            daemon=True,
        )
        for i in range(WORKER_COUNT)
    ]
    for worker in workers:
        worker.start()

    for worker in workers:
        worker.join()

    print(f"\nOdwiedzono {len(visited)} stron.")