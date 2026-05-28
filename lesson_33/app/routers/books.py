from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.schemas import BookCreate, BookResponse, AuthorResponse
from app.db import AUTHORS, BOOKS

from app.dependencies import verify_api_key

router = APIRouter(
    prefix="/books",
    tags=["Books"],
)

@router.get("/", response_model=dict[int, BookResponse], dependencies=[Depends(verify_api_key)])
async def get_books():
    """
    Pobiera listę książek.

    Example response:
    ```json
    {
        "1": {
            "id": 1,
            "name": "Harry Potter",
            "year": 1997,
            "author": {
                "id": 1,
                "name": "J.K. Rowling",
                "age": 40,                
                "email": "mail@mail.com"
            }
        }
    }
    ```
    """
    return BOOKS


@router.post("/", response_model=BookResponse, status_code=201, dependencies=[Depends(verify_api_key)])
async def add_book(book: BookCreate):
    """
    Tworzy nową książkę.

    Request example:
    ```json
    {
        "name": "Harry Potter",
        "year": 1997,
        "author": {
            "name": "J.K. Rowling",     
            "email": "mail@mail.com"
        }
    }
    ```

    Response example:
    ```json
    {
        "id": 1,
        "name": "Harry Potter",
        "year": 1997,
        "author": {
            "id": 1,
            "name": "J.K. Rowling",   
            "email": "mail@mail.com"
        }
    }
    ```
    """
    
    author_id = max(AUTHORS.keys(), default=0) + 1

    author_obj = AuthorResponse(
        id=author_id,
        name=book.author.name,
        email=book.author.email
    )

    AUTHORS[author_id] = author_obj.model_dump()

    book_id = max(BOOKS.keys(), default=0) + 1

    new_book = BookResponse(
        id=book_id,
        name=book.name,
        year=book.year,
        author=author_obj
    )

    BOOKS[book_id] = new_book.model_dump()
    return new_book



@router.get("/{id}", response_model=BookResponse, dependencies=[Depends(verify_api_key)])
async def get_book(id: int):
    """
    Pobiera książkę po ID.

    Path params:
        id (int): ID książki

    Example response:
    ```json
    {
        "id": 1,
        "name": "Harry Potter",
        "year": 1997,
        "author": {
            "id": 1,
            "name": "J.K. Rowling",
            "age": 40,                
            "email": "mail@mail.com"
        }
    }
    ```
    """
    book = BOOKS.get(id)

    if not book:
        raise HTTPException(status_code=404, detail="Not Found")

    return book



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(verify_api_key)])
async def delete_book(id: int):
    """
    Usuwa książkę po ID.

    Path params:
        id (int): ID książki
    """
    if id not in BOOKS:
        raise HTTPException(status_code=404, detail="Not Found")

    del BOOKS[id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)