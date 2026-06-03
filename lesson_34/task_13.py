import asyncio
from aiohttp import web

rooms = {}

def get_room(room_id):
    return rooms.setdefault(room_id, set())


def add_to_room(ws, room_id):
    ws.room_id = room_id
    get_room(room_id).add(ws)


def remove_from_room(ws):
    if ws.room_id in rooms:
        rooms[ws.room_id].discard(ws)

        if not rooms[ws.room_id]:
            del rooms[ws.room_id]


async def broadcast_message(sender, message, nick):
    room = rooms.get(sender.room_id, set())
    disconnected = []

    for conn in room:
        if conn != sender:
            try:
                await conn.send_json({
                    "nick": nick,
                    "message": message
                })
            except Exception:
                disconnected.append(conn)

    for conn in disconnected:
        room.discard(conn)


async def handle_join(ws, data):
    room_id = data.get("room_id")
    nick = data.get("nick")

    if not nick:
        await ws.send_json({"error": "Nick is required"})
        await ws.close()
        return False

    ws.nick = nick
    add_to_room(ws, room_id)

    await ws.send_json({
        "message": f"Joined room {room_id}"
    })

    await broadcast_message(
        ws,
        f"{nick} joined the room",
        "SYSTEM"
    )

    print(f"{nick} joined room {room_id}")
    return True


async def handle_message(ws, data):
    message = data.get("message", "")
    print(f"[{ws.room_id}] {ws.nick}: {message}")

    await broadcast_message(ws, message, ws.nick)


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    ws.room_id = None
    ws.nick = None

    await ws.send_str("Send JSON: {room_id, nick}")

    print("Client connected")

    try:
        async for msg in ws:

            if msg.type != web.WSMsgType.TEXT:
                continue

            data = msg.json()

            # first message = join
            if ws.room_id is None:
                ok = await handle_join(ws, data)
                if not ok:
                    return ws
                continue

            await handle_message(ws, data)

    finally:
        if ws.room_id is not None:
            await broadcast_message(
                ws,
                f"{ws.nick} left the room",
                "SYSTEM"
            )

            remove_from_room(ws)

    return ws

app = web.Application()
app.router.add_get("/ws", websocket_handler)


if __name__ == "__main__":
    print("🚀 WebSocket chat rooms running on ws://localhost:8080/ws")
    web.run_app(app, host="localhost", port=8080)