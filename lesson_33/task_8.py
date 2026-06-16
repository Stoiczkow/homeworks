"""
Dla dowolnego API dodaj:
· Tytuł i opis aplikacji
· Tagi do endpoints
· Docstringi z przykładami
Sprawdź /docs.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Zadanie 8 - Dokumentacja",
    description="Proste API demonstrujące dokumentację FastAPI.",
    version="1.0.0",
)


@app.get("/", tags=["Info"])
async def root():
    """
    Zwraca prostą wiadomość powitalną.

    Przykład:
    GET / {"message": "Witaj w API dokumentacyjnym"}
    """
    return {"message": "Witaj w API dokumentacyjnym"}


@app.get("/items", tags=["Items"])
async def list_items(limit: int = 10):
    """
    Zwraca listę przykładowych elementów.

    Przykład:
    GET /items?limit=3 -> ["Item 0", "Item 1", "Item 2"]
    """
    return [f"Item {i}" for i in range(limit)]
