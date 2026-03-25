"""
7.
Parser URL: Napisz funkcję parse_url(url: str) -> dict , która przyjmuje jako
argument adres URL w formie stringa (np.
https://api.example.com:8080/users/search?active=true ) i zwraca słownik
zawierający jego części: protocol , domain , port i path .
Dla podanego przykładu, wynik powinien być: {'protocol': 'https', 'domain':
'api.example.com', 'port': 8080, 'path': '/users/search?active=true'} .
Obsłuż przypadek, gdy port nie jest podany (dla http domyślny to 80, dla https 443).
Wskazówka: Użyj metod do manipulacji stringami, takich jak split() czy find() .
"""


def parse_url(url: str) -> dict:
    if "://" not in url:
        raise ValueError("URL musi zawierac protocol://")

    protocol, rest = url.split("://", 1)

    slash_index = rest.find("/")
    query_index = rest.find("?")

    if slash_index == -1:
        if query_index == -1:
            authority = rest
            path = "/"
        else:
            authority = rest[:query_index]
            path = "/" + rest[query_index:]
    else:
        authority = rest[:slash_index]
        path = rest[slash_index:]

    if ":" in authority:
        domain, port_str = authority.rsplit(":", 1)
        port = int(port_str)
    else:
        domain = authority
        if protocol == "http":
            port = 80
        elif protocol == "https":
            port = 443
        else:
            port = None

    return {
        "protocol": protocol,
        "domain": domain,
        "port": port,
        "path": path,
    }


if __name__ == "__main__":
    url_with_port = "https://api.example.com:8080/users/search?active=true"
    url_without_port = "http://example.com/articles"

    print(parse_url(url_with_port))
    print(parse_url(url_without_port))
