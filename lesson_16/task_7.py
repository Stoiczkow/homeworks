def parse_url(url: str) -> dict:
    protocol, rest = url.split("://", 1)

    slash_index = rest.find("/")
    if slash_index != -1:
        host_part = rest[:slash_index]
        path = rest[slash_index:]
    else:
        host_part = rest
        path = "/"

    if ":" in host_part:
        domain, port_str = host_part.split(":", 1)
        port = int(port_str)
    else:
        domain = host_part
        port = 443 if protocol == "https" else 80

    return {
        "protocol": protocol,
        "domain": domain,
        "port": port,
        "path": path
    }


urls = [
    "https://api.example.com:8080/users/search?active=true",
    "http://example.com/index.html",
    "https://secure.site.org/login",
    "http://localhost:3000/api/data",
]

for url in urls:
    result = parse_url(url)
    print(f"URL:      {url}")
    print(f"Wynik:    {result}")
    print()
