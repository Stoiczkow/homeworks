"""
Podziel aplikację z książkami na moduły:
· routers/books.py - endpoints książek
· routers/authors.py - endpoints autorów
· main.py - dołącz routery
"""

from fastapi import FastAPI
from routers import books, authors

app = FastAPI(title="Zadanie 9 - APIRouter")

app.include_router(books.router)
app.include_router(authors.router)


@app.get("/")
async def root():
    return {"message": "API książek i autorów"}
