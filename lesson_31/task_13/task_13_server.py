import asyncio


async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()

    address = writer.get_extra_info("peername")
    print(f"Otrzymano od {address}: {message}")

    writer.write(data)
    await writer.drain()

    print("Odesłano wiadomość do klienta.")

    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(
        handle_client,
        "127.0.0.1",
        8888
    )

    address = server.sockets[0].getsockname()
    print(f"Serwer działa na {address}")

    async with server:
        await server.serve_forever()


asyncio.run(main())