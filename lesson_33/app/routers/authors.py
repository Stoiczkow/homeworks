from fastapi import APIRouter, HTTPException, Response, status

from app.schemas import AuthorCreate, AuthorResponse
from app.db import AUTHORS

router = APIRouter(
    prefix="/authors",
    tags=["Authors"],
)

@router.get("/", response_model=dict[int, AuthorResponse])
async def get_authors():
    """
    Pobiera listę wszystkich autorów.

    Example response:
    ```json
    {
        "1": {
            "id": 1,
            "name": "J.K. Rowling",
            "email": "mail1@mail.com"
        },
        "2": {
            "id": 2,
            "name": "George Orwell",
            "email": "mail2@mail.com"
        }
    }
    ```
    """
    return AUTHORS


@router.post("/", response_model=AuthorResponse, status_code=201)
async def add_author(author: AuthorCreate):
    """
    Dodaje nowego autora.

    Request example:
    ```json
    {
        "name": "J.K. Rowling",
        "email": "mail1@mail.com"
    }
    ```

    Response example:
    ```json
    {
        "id": 1,
        "name": "J.K. Rowling",
        "email": "mail1@mail.com"
    }
    ```
    """

    author_id = max(AUTHORS.keys(), default=0) + 1

    new_author = AuthorResponse(
        id=author_id,
        **author.model_dump()
    )

    AUTHORS[author_id] = new_author.model_dump()

    return new_author
