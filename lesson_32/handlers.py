from json import JSONDecodeError, dumps

from aiohttp import web
from sqlalchemy import select, update, delete
import asyncio

from models import Product, Account, User

from datetime import datetime

async def mainpage(request: web.Request):
    return web.Response(
        body="<h1>Witaj na mojej stronie!</h1>",
        content_type="text/html"
        )

async def hello_to_user(request: web.Request):
    name = request.match_info.get("imie")
    if name == "admin":
        raise web.HTTPForbidden(text="Dostęp dla admina zabroniony")
    return web.Response(
    body=f"<h1>Witaj {name}</h1>",
    content_type="text/html"
    )

async def simple_api(request: web.Request):
    info = {"status": "OK", "server_time": f"{str(datetime.now())}"}
    return web.json_response(info)

async def api_search(request: web.Request):
    q = request.query.get("q")
    if q:
        return web.json_response({"szukana fraza": f"{q}"})
    else:
        raise web.HTTPNotFound(
            text=dumps({"błąd": "brak parametru q"}),
            content_type="application/json"
            )

async def api_echo(request: web.Request):

    if request.content_type == 'application/json':
        try:
            json_data = await request.json()
        except JSONDecodeError:
            raise web.HTTPBadRequest(text="Niepoprawny format JSON")
        return web.json_response(json_data)
    else:
        raise web.HTTPBadRequest(
            text=dumps({"error": "Invalid data or headers"}), content_type="application/json"
            )

async def add_product(request: web.Request):
    try:
        data = await request.json()
    except JSONDecodeError:
        raise web.HTTPBadRequest(
            text=dumps({"error": "Invalid data"}), content_type="application/json"
        )
    print(data)

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:

        async with session.begin():
            new_product = Product(name=data["name"], price=data["price"], user_id=data["user"])
            session.add(new_product)
            await session.flush()
            product = new_product.to_dict()

    return web.json_response(product, status=201)

async def get_all_products(request: web.Request):
    '''
    Po zadaniu 17 nie pobiera wszystkich produktów, tylko
    paginuje
    '''
    session_factory = request.app["db_session_factory"]
    try:
        page = int(request.query.get("page"))
        limit = int(request.query.get("limit"))
    except (ValueError, TypeError):
        page = 1
        limit = 10
    
    chosen_offset = (page - 1) * limit

    async with session_factory() as session:
        select_products = select(Product).limit(limit).offset(chosen_offset)

        result = await session.execute(select_products)

        result = result.scalars().all()

    products = [product.to_dict() for product in result]

    return web.json_response(products)

async def get_single_product(request: web.Request):
    
    product_id = request.match_info.get("id")
    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        try:
            select_product = select(Product, User.name).join(User).where(Product.id==int(product_id))
        except ValueError:
            raise web.HTTPBadRequest(
            text=dumps({"Error": f"Invalid product ID"}),
            content_type="application/json"
            )

        result = await session.execute(select_product)
        product = result.first()

        if product:
            product_obj, user_name = product
            result_dict: dict = product_obj.to_dict()
            result_dict["username"] = user_name
            return web.json_response(result_dict)
        
        raise web.HTTPNotFound(
            text=dumps({"Error": f"Product with id {product_id} not found"}),
            content_type="application/json"
            )
    
async def update_product(request: web.Request):
    
    product_id = request.match_info.get("id")
    session_factory = request.app["db_session_factory"]

    body = await request.json()

    try:
        new_name = body.get("name")
        new_price = body.get("price")
    except:
        raise web.BaseRequest(
        text=dumps({"Error": "Posted data invalid"}),
        content_type="application/json"
        )

    async with session_factory() as session:
        try:
            select_product = select(Product).where(Product.id==int(product_id))
        except ValueError:
            raise web.HTTPBadRequest(
            text=dumps({"Error": f"Invalid product ID"}),
            content_type="application/json"
            )

        result = await session.execute(select_product)
        product = result.scalar_one_or_none()

        if not product:    
            raise web.HTTPNotFound(
                text=dumps({"Error": f"Product with id {product_id} not found"}),
                content_type="application/json"
                )
                    
        patch_product_sql = update(Product).where(Product.id==int(product_id)).values(name=new_name, price=new_price)
        try:
            await session.execute(patch_product_sql)
            await session.commit()
        except:
            await session.rollback()
            raise web.HTTPBadRequest(
            text=dumps({"Error": f"Couldn't save the data in the database"}),
            content_type="application/json"
            )
        
    return web.json_response({"id": f"{product_id}", "name": f"{new_name}", "price": f"{new_price}"})

async def delete_product(request: web.Request):
    
    product_id = request.match_info.get("id")
    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        try:
            select_product = select(Product).where(Product.id==int(product_id))
        except ValueError:
            raise web.HTTPBadRequest(
            text=dumps({"Error": f"Invalid product ID"}),
            content_type="application/json"
            )

        result = await session.execute(select_product)
        product = result.scalar_one_or_none()

        if not product:    
            raise web.HTTPNotFound(
                text=dumps({"Error": f"Product with id {product_id} not found"}),
                content_type="application/json"
                )
                    
        delete_query = delete(Product).where(Product.id==int(product_id))
        try:
            await session.execute(delete_query)
            await session.commit()
        except:
            await session.rollback()
            raise web.HTTPBadRequest(
            text=dumps({"Error": f"Couldn't perform this operation"}),
            content_type="application/json"
            )
        
    return web.HTTPNoContent()

async def transfer(request: web.Request):

    if request.content_type == 'application/json':
        try:
            json_data = await request.json()
        except JSONDecodeError:
            raise web.HTTPBadRequest(text="Niepoprawny format JSON")
    else:
        raise web.HTTPBadRequest(
            text=dumps({"error": "Invalid data or headers"}),
                content_type="application/json"
                )
    try:
        from_id = int(json_data["from_id"])
        to_id = int(json_data["to_id"])
        amount = int(json_data["amount"])
        
    except (ValueError, KeyError):
        raise web.HTTPBadRequest(
            text=dumps({"error": "Invalid data"}),
                content_type="application/json"
                )

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        async with session.begin():

            select_first_account = select(Account).where(Account.id==from_id).with_for_update()
            select_second_account = select(Account).where(Account.id==to_id).with_for_update()

            result_from = await session.execute(select_first_account)
            result_to = await session.execute(select_second_account)
            account_from = result_from.scalar_one_or_none()
            account_to = result_to.scalar_one_or_none()

            if not account_from or not account_to:
                raise web.HTTPBadRequest(
                text=dumps({"Error": f"Invalid accounts"}),
                content_type="application/json")
            
            if account_from.balance < amount:
                raise web.HTTPConflict(
                text=dumps({"Error": f"Not enough money on the account"}),
                content_type="application/json")
            else:
                account_from.balance -= amount
                account_to.balance += amount
            
            return web.json_response({"Success": "Transfer completed"})
        
async def chat(request: web.Request):

    if request.content_type == 'application/json':
        try:
            json_data = await request.json()
        except JSONDecodeError:
            raise web.HTTPBadRequest(text="Niepoprawny format JSON")
    else:
        raise web.HTTPBadRequest(
            text=dumps({"error": "Invalid data or headers"}),
                content_type="application/json"
                )
    try:
        prompt_text = str(json_data["prompt"])
        
    except (ValueError, KeyError):
        raise web.HTTPBadRequest(
            text=dumps({"error": "Invalid data"}),
                content_type="application/json"
                )

    await asyncio.sleep(3)
    return web.json_response({"response": f"Otrzymałem twój prompt: '{prompt_text}' i przetworzyłem go."})