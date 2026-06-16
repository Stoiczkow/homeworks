from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Dict

router = APIRouter(prefix="/books", tags=["Books"])


class Book(BaseModel):
    title: str = Field(..., min_length=1)
    author_id: int


books_db: Dict[int, Book] = {}
book_id_counter = 1


@router.get("/")
async def list_books():
    return [{"id": bid, **book.model_dump()} for bid, book in books_db.items()]


@router.get("/{book_id}")
async def get_book(book_id: int):
    book = books_db.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Książka nie istnieje")
    return {"id": book_id, **book.model_dump()}


@router.post("/")
async def create_book(book: Book):
    global book_id_counter
    books_db[book_id_counter] = book
    book_id_counter += 1
    return {"id": book_id_counter - 1, **book.model_dump()}
