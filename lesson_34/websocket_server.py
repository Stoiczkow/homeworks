from aiohttp import web


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:

        if msg.type == web.WSMsgType.TEXT:
            try:
                data = msg.json()

                print(data)

                await ws.send_json({
                    "room": data.get("room"),
                    "message": data.get("message")
                })

            except Exception as e:
                await ws.send_json({
                    "error": "Invalid JSON",
                    "details": str(e)
                })

        elif msg.type == web.WSMsgType.ERROR:
            print(f"Błąd: {ws.exception()}")

    return ws


app = web.Application()
app.router.add_get("/ws", websocket_handler)

if __name__ == "__main__":
    print("🚀 Chat server działa na ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)