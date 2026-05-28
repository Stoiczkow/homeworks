from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.schemas import AuthorCreate, AuthorResponse, BookResponse
from app.models import AuthorORM, BookORM


router = APIRouter(
    prefix="/authors",
    tags=["Authors"],
)


@router.get("/", response_model=List[AuthorResponse])
async def get_authors(db: AsyncSession = Depends(get_db)):
    """
    Pobiera listę wszystkich autorów.
    """

    result = await db.execute(
        select(AuthorORM)
    )

    authors = result.scalars().all()

    return authors

@router.get("/{author_id}/books", response_model=List[BookResponse])
async def get_author_books(
    author_id: int,
    db: AsyncSession = Depends(get_db)
    ):
    """
    Pobiera listę wszystkich ksiazek autora z ID.
    """

    result = await db.execute(
        select(BookORM)
        .options(selectinload(BookORM.author))
        .where(BookORM.author_id == author_id)
    )

    author_books = result.scalars().unique().all()

    return author_books


@router.post("/", response_model=AuthorResponse, status_code=201)
async def add_author(
    author: AuthorCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Dodaje nowego autora do bazy danych.

    Args:
        author: Dane autora
        db: Sesja bazy danych
    """

    result = await db.execute(
        select(AuthorORM).where(
            AuthorORM.email == author.email
        )
    )

    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=400,
            detail="Author already exists"
        )

    db_author = AuthorORM(
        **author.model_dump()
    )

    db.add(db_author)

    await db.commit()

    await db.refresh(db_author)

    return db_author