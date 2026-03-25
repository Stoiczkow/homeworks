# Model żądania: Utwórz w Pythonie słownik, który będzie reprezentował żądanie GET w
# celu pobrania listy wszystkich artykułów z adresu /api/articles . W nagłówkach dodaj
# klucz Host z wartością my-blog.com 

request = {
    "start_line": {
        "method": "GET",
        "target": "/api/articles",
        "version": "HTTP/1.1"
        },
    "headers": {
        "Host": "my-blog.com",
        "User-Agent": "python-requests",
        "Accept": "application/json"
        },
    "body": None
    }