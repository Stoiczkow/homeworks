from fastapi import APIRouter, HTTPException
from main import BOOKS_DB, Book, BookResponse

router = APIRouter(
prefix="/books",
tags=["Books"],
)

@router.get("/", tags=["Objects"])
async def get_books():
    return BOOKS_DB

@router.get("/{id}", tags=["Objects"])
async def get_specific_book(id: int):
    """Ta funkcja pozwala na pobranie dowolnej książki z istniejących
    Dokonaj requestu na URL /books/{id} a w miejscu {id} podaj ID
    żądanej książki. W przypadku powodzenia otrzymasz jej dane oraz odpowiedź 204;
    Gdy książka z takim ID nie istnieje, otrzymasz błąd 404."""
    
    return BOOKS_DB.get(id)

@router.post("/", response_model=BookResponse, status_code=201, tags=["Objects"])
async def get_books(book: Book):
    try:
        book_values = book.model_dump()
        BOOKS_DB[book_values["id"]] = book_values
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"{e}")

    return book

@router.delete("/{id}", status_code=204, tags=["Objects"])
async def delete_specific_book(id: int):
    try:
        BOOKS_DB[id]
    except KeyError:
        raise HTTPException(status_code=404)