import asyncio
from aiohttp import web


async def chat_handler(request: web.Request):
    try:
        data = await request.json()
        prompt_text = data["prompt"]
    except Exception:
        raise web.HTTPBadRequest(text="Oczekiwano JSON z polem 'prompt'")

    await asyncio.sleep(3)

    return web.json_response({
        "response": f"Otrzymałem twój prompt: '{prompt_text}' i przetworzyłem go."
    })


def create_app():
    app = web.Application()

    app.router.add_post("/api/v1/chat", chat_handler)

    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app, host="127.0.0.1", port=8080)