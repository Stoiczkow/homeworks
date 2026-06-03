import aiohttp
import asyncio

async def receiver(ws):
    async for response in ws:
        if response.type == aiohttp.WSMsgType.JSON:
            print(f"Otrzymano: {response.data}")
        
async def sender(ws):
    messages = ["Cześć!", "Jak się masz?", "Do widzenia!"]
    msg_json = {
            "room": "room_1"
    }
    for _ in range(3):
        await ws.send_json({
            "room": "room_1"
        })                    
        print(f"Wysłano wiadomość: {msg_json}")
        
        await asyncio.sleep(1)

async def websocket_client():
    async with aiohttp.ClientSession() as session:
        
        async with session.ws_connect('ws://localhost:8080/ws') as ws:
            print("Połączono z serwerem")
            
            receiver_task = asyncio.create_task(receiver(ws))            
            await sender(ws)
            
            await ws.close()
            print("Połączenie zamknięte!")
            receiver_task.cancel()

if __name__ == '__main__':
    asyncio.run(websocket_client())