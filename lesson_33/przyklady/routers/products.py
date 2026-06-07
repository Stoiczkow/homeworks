# === file: routers/products.py ===
from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)

products_db = {}


@router.get("/")
async def get_products():
    """Pobiera wszystkie produkty."""
    return list(products_db.values())


@router.get("/{product_id}")
async def get_product(product_id: int):
    """Pobiera produkt po ID."""
    return products_db.get(product_id, {})