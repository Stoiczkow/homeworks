# Napisz prosty crawler, który zaczyna od jednego adresu URL. Pobiera jego zawartość,
# znajduje w niej wszystkie linki do tej samej domeny, a następnie dodaje je do kolejki do
# odwiedzenia. Użyj puli wątków do jednoczesnego pobierania stron z kolejki. Ogranicz liczbę
# odwiedzonych stron do np. 50, aby nie "zalać" serwera. Użyj bezpiecznej wątkowo kolejki i
# zbioru (set) do przechowywania już odwiedzonych linków.

from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from queue import Queue
from threading import Lock
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen


class LinkParser(HTMLParser):
	def __init__(self):
		super().__init__()
		self.links = set()

	def handle_starttag(self, tag, attrs):
		if tag != "a":
			return

		for name, value in attrs:
			if name == "href" and value:
				self.links.add(value)


class SimpleCrawler:
	def __init__(self, start_url, max_pages=50, max_workers=5):
		self.start_url = self.prepare_start_url(start_url)
		self.max_pages = max_pages
		self.max_workers = max_workers
		self.domain = self.get_domain(self.start_url)
		self.to_visit = Queue()
		self.visited = set()
		self.scheduled = set()
		self.lock = Lock()

	@staticmethod
	def prepare_start_url(url):
		url = url.strip()
		if not url:
			return ""

		if not url.startswith(("http://", "https://")):
			url = "https://" + url

		return SimpleCrawler.normalize_url(url)

	@staticmethod
	def normalize_url(url, base_url=None):
		if base_url:
			url = urljoin(base_url, url)

		url, _ = urldefrag(url)
		parsed = urlparse(url)

		if parsed.scheme not in ("http", "https") or not parsed.netloc:
			return ""

		path = parsed.path or "/"
		return parsed._replace(
			scheme=parsed.scheme.lower(),
			netloc=parsed.netloc.lower(),
			path=path,
			fragment="",
		).geturl()

	@staticmethod
	def get_domain(url):
		hostname = urlparse(url).hostname or ""
		hostname = hostname.lower()

		if hostname.startswith("www."):
			hostname = hostname[4:]

		return hostname

	def is_same_domain(self, url):
		return self.get_domain(url) == self.domain

	def fetch_html(self, url):
		try:
			request = Request(
				url,
				headers={"User-Agent": "Mozilla/5.0 (compatible; SimpleCrawler/1.0)"},
			)
			with urlopen(request, timeout=10) as response:
				content_type = response.headers.get("Content-Type", "")
				if "text/html" not in content_type:
					return ""

				encoding = response.headers.get_content_charset() or "utf-8"
				return response.read().decode(encoding, errors="ignore")
		except Exception as error:
			print(f"Błąd pobierania {url}: {error}")
			return ""

	def extract_links(self, html, base_url):
		parser = LinkParser()
		parser.feed(html)
		parser.close()

		links = set()
		for link in parser.links:
			normalized_link = self.normalize_url(link, base_url)
			if normalized_link and self.is_same_domain(normalized_link):
				links.add(normalized_link)

		return links

	def worker(self):
		while True:
			url = self.to_visit.get()

			try:
				if url is None:
					return

				with self.lock:
					if url in self.visited:
						continue

					self.visited.add(url)
					current_count = len(self.visited)

				print(f"[{current_count}/{self.max_pages}] Odwiedzam: {url}")

				html = self.fetch_html(url)
				if not html:
					continue

				for link in self.extract_links(html, url):
					with self.lock:
						if link in self.scheduled:
							continue

						if len(self.scheduled) >= self.max_pages:
							break

						self.scheduled.add(link)
						self.to_visit.put(link)
			finally:
				self.to_visit.task_done()

	def crawl(self):
		if not self.start_url or not self.domain:
			print("Podaj poprawny adres URL.")
			return set()

		self.scheduled.add(self.start_url)
		self.to_visit.put(self.start_url)

		with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
			for _ in range(self.max_workers):
				executor.submit(self.worker)

			self.to_visit.join()

			for _ in range(self.max_workers):
				self.to_visit.put(None)

			self.to_visit.join()

		return self.visited


if __name__ == "__main__":
	start_url = input("Podaj adres startowy (np. https://example.com): ").strip()

	crawler = SimpleCrawler(start_url=start_url, max_pages=50, max_workers=5)
	visited_links = crawler.crawl()

	print("\nOdwiedzone strony:")
	for url in sorted(visited_links):
		print(url)

