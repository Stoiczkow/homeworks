'''
    Zadanie 7 - Parser URL: Napisz funkcję parse_url(url: str) -> dict , która przyjmuje jako
    argument adres URL w formie stringa (np. https://api.example.com:8080/users/search?active=true ) i zwraca słownik
    zawierający jego części: protocol , domain , port i path .

    Dla podanego przykładu, wynik powinien być: {'protocol': 'https', 'domain':
    'api.example.com', 'port': 8080, 'path': '/users/search?active=true'} .

    Obsłuż przypadek, gdy port nie jest podany (dla http domyślny to 80, dla https 443).

    Wskazówka: Użyj metod do manipulacji stringami, takich jak split() czy find() 
'''

def parse_url(url: str) -> dict:
    protocol_split = url.split("://", 1)
    protocol = protocol_split[0]
    rest = protocol_split[1]

    slash_index = rest.find("/")
    domain_port = rest[:slash_index]
    path = rest[slash_index:] 

    if ":" in domain_port:
        domain, port_str = domain_port.split(":", 1)
        port = int(port_str)
    else:
        domain = domain_port

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
        "path": path
    }

url = "https://api.example.com:8080/users/search?active=true"
print(parse_url(url))
