import asyncio
import time

from aiohttp import web

active_connections = []

async def send_ping(ws):
    try:
        while True:
            await asyncio.sleep(30)

            if time.time() - ws.pong_time > 60:
                await ws.close()
                break

            try:
                print("wysylam ping")
                await ws.send_str("ping")
            except Exception:
                break

    except asyncio.CancelledError:
        pass
               
async def websocket_handler(request):
    ws = web.WebSocketResponse()
    
    await ws.prepare(request)
    
    active_connections.append(ws)
    
    ws.pong_time = time.time()
    
    ping_task = asyncio.create_task(send_ping(ws))    
    
    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                print(msg.data)
                
                if msg.data == 'pong':
                    ws.pong_time = time.time()
                    continue

                print("message:", msg.data)
                
            elif msg.type == web.WSMsgType.ERROR:
                print("Websocket error") 
                       
    finally:
        ping_task.cancel()

        if ws in active_connections:
            active_connections.remove(ws)

        print(f"Klient rozlaczony. Zostało {len(active_connections)}")
    
    return ws

app = web.Application()

app.router.add_get('/ws', websocket_handler)

if __name__ == '__main__':
    print("Serwer działa na ws://localhost:8080/ws")
    web.run_app(app, host='localhost', port=8080)