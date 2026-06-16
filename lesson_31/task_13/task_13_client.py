import asyncio


async def main():
    reader, writer = await asyncio.open_connection(
        "127.0.0.1",
        8888
    )

    message = "Cześć serwerze!"
    print(f"Wysyłam: {message}")

    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f"Odpowiedź z serwera: {data.decode()}")

    writer.close()
    await writer.wait_closed()


asyncio.run(main())