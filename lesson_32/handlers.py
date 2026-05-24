from json import JSONDecodeError

from aiohttp import web
from sqlalchemy import select
from json import dumps

from models import Product, Account


async def add_product(request: web.Request):
    try:
        data = await request.json()
    except JSONDecodeError:
        raise web.HTTPBadRequest(
            text=dumps({"error": "Invalid data"}), content_type="application/json"
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

        results = result.scalars().all()

    products = [product.to_dict() for product in results]

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

    

async def update_product(request: web.Request):
    product_id = request.match_info.get("id")

    try:
            product_id = select(Product).where(Product.id == int(product_id))
    
    except ValueError:
            
            raise web.HTTPBadRequest(
                text=dumps({"message": f"Invalid id {product_id}"}),
                content_type="application/json",
            )

    try:
        data = await request.json()
    except JSONDecodeError:
        raise web.HTTPBadRequest(
            text=dumps({"error": "Invalid data"}), type="application/json"
        )

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        

        async with session.begin():
            select_product = select(Product).where(Product.id == int(product_id))

            result = await session.execute(select_product)

            product = result.scalar_one_or_none()

            if product is None:
                raise web.HTTPNotFound(
                    text=dumps(
                        {"message": f"Product with id {product_id} not found"}
                    ),
                    content_type="application/json",
                )

            if "name" in data:
                product.name = data["name"]

            if "price" in data:
                product.price = data["price"]

            await session.flush()

            updated_product = product.to_dict()

    return web.json_response(updated_product)

async def delete_product(request: web.Request):
    product_id = request.match_info.get("id")

    session_factory = request.app["db_session_factory"]
    async with session_factory() as session:
        async with session.begin():
            select_product = select(Product).where(Product.id == int(product_id))

            result = await session.execute(select_product)

            product = result.scalar_one_or_none()

            if product is None:

                raise web.HTTPNotFound(
                    text=dumps(
                        {"message": f"Product with id {product_id} not found"}
                    ),
                    content_type="application/json",
                )

            await session.delete(product)
    
    return web.Response(status=204)


async def transfer(request: web.Request):
    try:
        data = await request.json()
    except JSONDecodeError:
        raise web.HTTPBadRequest(
            text=dumps({"error": "Invalid data"}), type="application/json"
        )
    
    from_id = data["from"]