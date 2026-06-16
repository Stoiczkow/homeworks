'''
Dodaj odpowiednie status codes:
201 dla POST
204 dla DELETE
404 gdy książka nie istnieje
'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

books: dict[int, dict] = {}
next_id = 1

class Book(BaseModel):
    title: str = Field(..., min_length=2, max_length=100)
    author: str = Field(..., min_length=2, max_length=100)

@app.get("/books")
def get_books():
    return list(books.values())

@app.get("/books/{id}")
def get_book(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="Książka nie istnieje")
    return books[id]

@app.post("/books", status_code=201)
def add_book(book: Book):
    global next_id
    new_book = {
        "id": next_id,
        "title": book.title,
        "author": book.author
    }
    books[next_id] = new_book
    next_id += 1
    return new_book

@app.delete("/books/{id}", status_code=204)
def delete_book(id: int):
    if id not in books:
        raise HTTPException(status_code=404, detail="Książka nie istnieje")
    books.pop(id)
    return None