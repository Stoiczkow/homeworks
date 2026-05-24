from fastapi import APIRouter, Depends
from pydantic import BaseModel

from dependencies import verify_api_key

router = APIRouter(
    prefix="/authors",
    tags=["Authors"],
)

authors_db = {}
author_id_counter = 1


class Author(BaseModel):
    name: str
    email: str
    


@router.get("/")
async def get_authors(api_key: str = Depends(verify_api_key)):
    return list(authors_db.values())


@router.post("/")
async def create_author(author: Author, api_key: str = Depends(verify_api_key)):
    global author_id_counter

    new_author = author.model_dump()
    new_author["id"] = author_id_counter

    authors_db[author_id_counter] = new_author
    author_id_counter += 1

    return new_author