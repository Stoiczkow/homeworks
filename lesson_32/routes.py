from handlers import (add_product,
                    get_all_products,
                    get_single_product,
                    mainpage,
                    hello_to_user,
                    simple_api,
                    api_search,
                    api_echo,
                    update_product,
                    delete_product,
                    transfer,
                    chat)

def setup_routes(app):
    app.router.add_get('/', mainpage)
    app.router.add_get('/witaj/{imie}', hello_to_user)
    app.router.add_get('/api/status', simple_api)
    app.router.add_get('/api/search', api_search)
    app.router.add_post('/api/echo', api_echo)
    app.router.add_post('/products', add_product)
    app.router.add_get('/products', get_all_products)
    app.router.add_get('/products/{id}', get_single_product)
    app.router.add_patch('/products/{id}', update_product)
    app.router.add_delete('/products/{id}', delete_product)
    app.router.add_post('/transfer', transfer)
    app.router.add_post('/api/v1/chat', chat)