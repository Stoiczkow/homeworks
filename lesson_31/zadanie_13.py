import asyncio


async def handle_echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print(f"Odebrano od {addr}: {message!r}")

    writer.write(data)
    await writer.drain()

    writer.close()
    await writer.wait_closed()


async def main() -> None:
    server = await asyncio.start_server(handle_echo, "127.0.0.1", 8888)
    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serwer echa nasłuchuje na {addrs}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSerwer zatrzymany.")
