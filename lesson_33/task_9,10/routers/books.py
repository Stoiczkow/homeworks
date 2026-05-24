from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel

from dependencies import verify_api_key

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)

books_db = {}
book_id_counter = 1


class Book(BaseModel):
    title: str
    author: str
    year: int


@router.get("/")
async def get_books(api_key: str = Depends(verify_api_key)):
    return list(books_db.values())


@router.get("/{book_id}")
async def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")

    return books_db[book_id]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    global book_id_counter

    new_book = book.model_dump()
    new_book["id"] = book_id_counter

    books_db[book_id_counter] = new_book
    book_id_counter += 1

    return new_book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")

    del books_db[book_id]
    return None