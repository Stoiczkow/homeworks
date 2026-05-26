import aiohttp
import asyncio


async def websocket_client():
    """
    Prosty klient WebSocket łączący się z serwerem
    i wysyłający kilka wiadomości.
    """
    # Tworzymy sesję HTTP (potrzebna do WebSocket)
    async with aiohttp.ClientSession() as session:

        # Łączymy się z serwerem WebSocket
        async with session.ws_connect("ws://localhost:8080/ws") as ws:
            print("✅ Połączono z serwerem!")

            # Wysyłamy kilka wiadomości
            messages = ["Cześć!", "Jak się masz?", "Do widzenia!"]

            for msg in messages:
                # Wysyłamy wiadomość tekstową
                await ws.send_str(msg)
                print(f"📤 Wysłano: {msg}")

                # Czekamy na odpowiedź
                response = await ws.receive()
                if response.type == aiohttp.WSMsgType.TEXT:
                    print(f"📥 Otrzymano: {response.data}")

                # Małe opóźnienie między wiadomościami
                await asyncio.sleep(1)

            # Zamykamy połączenie
            await ws.close()
            print("❌ Połączenie zamknięte")


# Uruchomienie klienta
if __name__ == "__main__":
    asyncio.run(websocket_client())