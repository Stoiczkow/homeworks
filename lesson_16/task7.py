# Parser URL: Napisz funkcję parse_url(url: str) -> dict , która przyjmuje jako
# argument adres URL w formie stringa (np.
# https://api.example.com:8080/users/search?active=true ) i zwraca słownik
# zawierający jego części: protocol , domain , port i path .
# Dla podanego przykładu, wynik powinien być: {'protocol': 'https', 'domain':
# 'api.example.com', 'port': 8080, 'path': '/users/search?active=true'} .
# Obsłuż przypadek, gdy port nie jest podany (dla http domyślny to 80, dla https 443).
# Wskazówka: Użyj metod do manipulacji stringami, takich jak split() czy find() .

# Zadanie 7

def parse_url(url: str) -> dict:

    dict_to_return = {}

    url_split1 = url.split(sep="://", maxsplit=1)
    dict_to_return.update({'protocol': url_split1[0]})

    url_split2 = url_split1[1].split(sep="/", maxsplit=1)
    dict_to_return.update({'path': url_split2[1]})

    domain_and_port_split = url_split2[0].split(sep=":", maxsplit=1)
    if len(domain_and_port_split) == 1:
        dict_to_return.update({'domain': domain_and_port_split[0]})
    else:
        dict_to_return.update({'domain': domain_and_port_split[0]})
        dict_to_return.update({'port': domain_and_port_split[1]})

    return dict_to_return

url = "https://api.example.com:8080/users/search?active=true"
url2 = "https://api.example.com/users/search?active=true"

print(f"Przykład pierwszy: {parse_url(url)}")
print(f"Przykład drugi: {parse_url(url2)}")