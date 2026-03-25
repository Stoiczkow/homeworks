"""
3. 
Model żądania: Utwórz w Pythonie słownik, który będzie reprezentował żądanie GET w
celu pobrania listy wszystkich artykułów z adresu /api/articles . W nagłówkach dodaj
klucz Host z wartością my-blog.com .
"""

request_get_articles = {
    "method": "GET",
    "target": "/api/articles",
    "headers": {
        "Host": "my-blog.com",
    },
}

print(request_get_articles)
