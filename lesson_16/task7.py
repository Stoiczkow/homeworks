# Parser URL: Napisz funkcję parse_url(url: str) -> dict , która przyjmuje jako
# argument adres URL w formie stringa (np.
# https://api.example.com:8080/users/search?active=true ) i zwraca słownik
# zawierający jego części: protocol , domain , port i path .
# Dla podanego przykładu, wynik powinien być: {'protocol': 'https', 'domain':
# 'api.example.com', 'port': 8080, 'path': '/users/search?active=true'} .
# Obsłuż przypadek, gdy port nie jest podany (dla http domyślny to 80, dla https 443).
# Wskazówka: Użyj metod do manipulacji stringami, takich jak split() czy find() .

def parse_url(url: str) ->dict:
    parts = url.split("://")
    protocol = parts[0]
    reszta = parts[1]

    reszta_p = reszta.split("/", 1)
    path = "/" + reszta_p[1]
    dom_port = reszta_p[0]

    if ":" in dom_port:
        d_p_parts = dom_port.split(":")
        domain = d_p_parts[0]
        port = int(d_p_parts[1])
    else:
        domain = dom_port
        if protocol == "http":
            port = 443
        elif protocol == "https":
            port = 80

    return  {
        "protocol": protocol,
        "domain": domain,
        "port": port,
        "path": path
        }
print(parse_url("https://api.example.com:8080/users/search?active=true"))
print(parse_url("https://api.example.com/users/search?active=true"))
print(parse_url("http://api.example.com/users/search?active=true"))
