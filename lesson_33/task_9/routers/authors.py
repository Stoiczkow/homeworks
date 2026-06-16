from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Dict

router = APIRouter(prefix="/authors", tags=["Authors"])


class Author(BaseModel):
    name: str = Field(..., min_length=1)


authors_db: Dict[int, Author] = {}
author_id_counter = 1


@router.get("/")
async def list_authors():
    return [{"id": aid, **author.model_dump()} for aid, author in authors_db.items()]


@router.get("/{author_id}")
async def get_author(author_id: int):
    author = authors_db.get(author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Autor nie istnieje")
    return {"id": author_id, **author.model_dump()}


@router.post("/")
async def create_author(author: Author):
    global author_id_counter
    authors_db[author_id_counter] = author
    author_id_counter += 1
    return {"id": author_id_counter - 1, **author.model_dump()}
