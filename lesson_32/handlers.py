from json import JSONDecodeError, dumps

from aiohttp import web
from sqlalchemy import select
from models import Product


async def add_product(request: web.Request):
    try:
        data = await request.json()
    except JSONDecodeError:
        raise web.HTTPBadRequest(
            text = dumps({"error": "Invalid data"}), content_type="application/json"
        )

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        

        async with session.begin():
            new_product = Product(name=data["name"], price=data["price"])
            session.add(new_product)

            await session.flush()

            product = new_product.to_dict()

    return web.json_response(product, status=201)

async def get_all_products(request: web.Request):
    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        select_products = select(Product)

        result = await session.execute(select_products)

        result = result.scalars().all()

    products = [product.to_dict() for product in result]

    return web.json_response(products)

async def get_single_product(request: web.Request):
    product_id = request.match_info.get("id")

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        try:
            select_product = select(Product).where(Product.id == int(product_id))
        except ValueError:
            raise web.HTTPBadRequest(
                text=dumps({"message": f"Invalid id {product_id}"}),
                content_type="application/json",
            )
        result = await session.execute(select_product)

        product = result.scalar_one_or_none()

        if product:
            return web.json_response(product.to_dict())

        raise web.HTTPNotFound(
            text=dumps({"message": f"Product with id {product_id} not found"}),
            content_type="application/json",
        )