from handlers import handle_home, handle_hello, handle_status, handle_search, handle_echo, add_product, get_all_products, get_product, update_product, delete_product, transfer, get_all_accounts, chat

def setup_routes(app):
    app.router.add_get("/", handle_home)
    app.router.add_get("/hello/{name}", handle_hello)
    app.router.add_get("/api/status", handle_status)
    app.router.add_get("/handle/search", handle_search)
    app.router.add_post("/api/echo", handle_echo)
    app.router.add_post("/products", add_product)
    app.router.add_get("/products", get_all_products)
    app.router.add_get("/products/{id}", get_product)
    app.router.add_post("/products/{id}", update_product)
    app.router.add_delete("/products/{id}", delete_product)
    app.router.add_get("/accounts", get_all_accounts)
    app.router.add_post("/transfer", transfer)
    app.router.add_post("/api/v1/chat", chat)