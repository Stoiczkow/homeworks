async def get_products(request: web.Request):
    try:
        page = int(request.query.get("page", 1))
        limit = int(request.query.get("limit", 10))
    except ValueError:
        raise web.HTTPBadRequest(text="Parametry page i limit muszą być liczbami")

    if page < 1:
        raise web.HTTPBadRequest(text="Parametr page musi być większy lub równy 1")

    if limit < 1:
        raise web.HTTPBadRequest(text="Parametr limit musi być większy lub równy 1")

    offset = (page - 1) * limit

    session_factory = request.app["db_session_factory"]

    async with session_factory() as session:
        stmt = select(Product).offset(offset).limit(limit)
        result = await session.execute(stmt)
        products = result.scalars().all()

        products_data = [product.to_dict() for product in products]

    return web.json_response({
        "page": page,
        "limit": limit,
        "products": products_data,
    })