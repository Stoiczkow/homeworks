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

print(parse_url(url2))