from fastapi import APIRouter

router = APIRouter(
    prefix="/authors",
    tags=["Authors"]
)

AUTHORS = [
    {"id": 1, "name": "Andrzej Sapkowski"},
    {"id": 2, "name": "J.K. Rowling"}
]


@router.get("/")
async def get_authors():
    """
    Pobiera listę autorów.
    """
    return AUTHORS