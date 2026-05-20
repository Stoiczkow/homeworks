from aiohttp import web

from zadanie_19_routes import setup_routes


def create_app() -> web.Application:
    app = web.Application()
    setup_routes(app)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), host="127.0.0.1", port=8080)