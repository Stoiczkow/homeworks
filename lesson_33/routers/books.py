from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

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


@router.get("/")
async def get_books():

    return BOOKS


@router.post(
    "/",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED
)
async def add_book(book: BookCreate):

    #Dodaje nową książkę.
    

    if not BOOKS:
        book_id = 1
    else:
        book_id = max(BOOKS.keys()) + 1

    new_book = book.model_dump()
    new_book["id"] = book_id

    BOOKS[book_id] = new_book

    return new_book


@router.get("/{id}", response_model=BookResponse)
async def get_book(id: int):


    book = BOOKS.get(id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return book


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_book(id: int):
    
    #Usuwa książkę po ID.
    

    book = BOOKS.get(id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    del BOOKS[id]