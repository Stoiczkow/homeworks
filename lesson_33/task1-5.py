# Stwórz aplikację FastAPI z trzema endpoints:

# GET / - zwraca {"message": "Hello"}
# GET /time - zwraca aktualny czas
# GET /random - zwraca losową liczbę 1-100

from fastapi import FastAPI, Path, HTTPException
from datetime import datetime
from random import randint
from pydantic import BaseModel, computed_field

app = FastAPI()

BOOKS = {}


class BookCreate(BaseModel):
    name: str
    year: int
    author: str


class BookResponse(BaseModel):
    id: int
    name: str
    year: int
    author: str


@app.get("/books")
async def get_books():
    return BOOKS


@app.post("/books", response_model=BookResponse)
async def add_book(book: BookCreate):
    if not BOOKS:
        id = 1
    else:
        id = max(list(BOOKS.keys())) + 1

    new_book = book.model_dump()
    new_book["id"] = id

    BOOKS[id] = new_book

    return new_book


@app.get("/books/{id}", response_model=BookResponse)
async def add_book(id: int):
    book = BOOKS.get(id)

    if not book:
        raise HTTPException(detail="Not Found", status_code=404)
    return book