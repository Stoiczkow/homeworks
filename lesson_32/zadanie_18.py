import asyncio

from aiohttp import web


async def chat(request: web.Request) -> web.Response:
    try:
        data = await request.json()
        prompt_text = data["prompt"]
    except (KeyError, TypeError):
        raise web.HTTPBadRequest(text="Oczekiwano JSON z polem 'prompt'")

    # symulacja długiego przetwarzania przez model AI
    await asyncio.sleep(3)

    return web.json_response({
        "response": f"Otrzymałem twój prompt: '{prompt_text}' i przetworzyłem go."
    })


app = web.Application()
app.router.add_post("/api/v1/chat", chat)


if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)