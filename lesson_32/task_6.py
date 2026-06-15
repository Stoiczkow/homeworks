"""
Stwórz handler POST na ścieżce /api/echo.
Handler ma odczytać dane JSON z request.json()
i odesłać je z powrotem w web.json_response.
"""

from aiohttp import web

async def echo_handler(request):
    dane = await request.json()
    return web.json_response(dane)

def main():
    app = web.Application()
    app.router.add_post("/api/echo", echo_handler)

    web.run_app(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()
