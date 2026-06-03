import asyncio

from aiohttp import web
import time

active_connections = []

async def broadcast_message(sender, message, nick):
    disconnected = []
    
    for conn in active_connections:
        if conn != sender:
            try:
                await conn.send_str(f"{nick}: {message}")
            except Exception:
                disconnected.append(conn)

    for conn in disconnected:
        active_connections.remove(conn)
    

async def websocket_handler(request):
    first_message = True
    nick = None
    
    ws = web.WebSocketResponse()
    
    await ws.prepare(request)
    
    start_time = asyncio.get_event_loop().time()
    
    active_connections.append(ws)
    print(f"Połączono nowego klienta! Łącznie połączeń: {len(active_connections)}")    
    
    await ws.send_str(f"Jesteś klientem nr {len(active_connections)}")
    
    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                if first_message:
                    nick = msg.data
                    first_message = False
                else:
                    if nick is None:
                        continue
                    print(f"Otrzymano: {msg.data}")
                
                    await broadcast_message(ws, msg.data, nick)
                
            elif msg.type == web.WSMsgType.ERROR:
                print(f"Błąd websocket {ws.exception()}")
    
    finally:
        if ws in active_connections:
            active_connections.remove(ws)
        end_time = asyncio.get_event_loop().time()
        
        print(f"Klient rozlaczony. Zostało {len(active_connections)}")
        print(f"Czas połączenia klienta: {end_time - start_time:.2f} s")
        await broadcast_message(ws, f"Użytkownik opuscil chat. Pozostalo: {len(active_connections)}", "system")   
           
    return ws
        

app = web.Application()

app.router.add_get('/ws', websocket_handler)

if __name__ == '__main__':
    print("Serwer działa na ws://localhost:8080/ws")
    web.run_app(app, host='localhost', port=8080)