from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

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


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get("/books")
async def get_books():
    return BOOKS


@app.post(
    "/books",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
async def add_book(book: BookCreate):

    if not BOOKS:
        book_id = 1
    else:
        book_id = max(BOOKS.keys()) + 1

    new_book = book.model_dump()
    new_book["id"] = book_id

    BOOKS[book_id] = new_book

    return new_book


@app.get("/books/{id}", response_model=BookResponse)
async def get_book(id: int):

    book = BOOKS.get(id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return book


@app.delete(
    "/books/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book(id: int):

    book = BOOKS.get(id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    del BOOKS[id]