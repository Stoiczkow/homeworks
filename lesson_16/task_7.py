# 7. Parser URL: Napisz funkcję parse_url(url: str) -> dict , która przyjmuje jako
# argument adres URL w formie stringa (np.
# https://api.example.com:8080/users/search?active=true ) i zwraca słownik
# zawierający jego części: protocol , domain , port i path .
# Dla podanego przykładu, wynik powinien być: {'protocol': 'https', 'domain':
# 'api.example.com', 'port': 8080, 'path': '/users/search?active=true'} .
# Obsłuż przypadek, gdy port nie jest podany (dla http domyślny to 80, dla https 443).
# Wskazówka: Użyj metod do manipulacji stringami, takich jak split() czy find() 

def parse_url(url: str) -> dict:
    split_1 = url.split('://', maxsplit=1)
    protocol = split_1[0]
    split_2 = split_1[1].split(':', maxsplit=1)
        
    if len(split_2) == 1:
        split_3 = split_2[0].split('/', maxsplit=1)
        domain = split_3[0]
        path = split_3[1]
            
        return {
            'protocol': protocol,
            'domain': domain,
            'path': path
        }
            
    else:            
        domain = split_2[0]
        split_3 = split_2[1].split('/', maxsplit=1)
        port = split_3[0]
        path = split_3[1]
        
        return {
            'protocol': protocol,
            'domain': domain,
            'port': port,
            'path': path
        }
        
    
url = "https://api.example.com:8080/users/search?active=true"
url2 = "https://api.example.com/users/search?active=true"  
    
print(parse_url(url))
print(parse_url(url2))