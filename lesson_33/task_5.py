"""
Stwórz proste CRUD API dla książek (dict w pamięci):
· GET /books - lista wszystkich
· GET /books/{id} - jedna książka
· POST /books - dodaj książkę
· DELETE /books/{id} - usuń książkę
(proste)
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict

app = FastAPI(title="Zadanie 5 - CRUD w pamięci")


class Book(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)


books_db: Dict[int, Book] = {}
book_id_counter = 1


@app.get("/books")
async def list_books():
    return [{"id": bid, **book.model_dump()} for bid, book in books_db.items()]


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    book = books_db.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Książka nie istnieje")
    return {"id": book_id, **book.model_dump()}


@app.post("/books", status_code=201)
async def create_book(book: Book):
    global book_id_counter
    books_db[book_id_counter] = book
    book_id_counter += 1
    return {"id": book_id_counter - 1, **book.model_dump()}


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Książka nie istnieje")
    del books_db[book_id]
    return {"detail": "Deleted"}
