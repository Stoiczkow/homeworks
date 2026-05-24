# === file: routers/users.py ===
from fastapi import APIRouter, HTTPException

# Tworzenie sub-routera z prefixem i tagami
router = APIRouter(
    prefix="/users",  # Wszystkie ścieżki będą zaczynać się od /users
    tags=["Users"],  # Tag dla dokumentacji
)

users_db = {}


@router.get("/")  # Faktyczna ścieżka: /users/
async def get_users():
    """Pobiera wszystkich użytkowników."""
    return list(users_db.values())


@router.get("/{user_id}")  # Faktyczna ścieżka: /users/{user_id}
async def get_user(user_id: int):
    """Pobiera użytkownika po ID."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]


@router.post("/")
async def create_user(user: dict):
    """Tworzy nowego użytkownika."""
    new_id = max(users_db.keys()) + 1 if users_db else 1
    user["id"] = new_id
    users_db[new_id] = user
    return user