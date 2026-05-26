# Pierwsza korutyna
# Napisz korutynę, która po uruchomieniu wypisze
# na konsolę "Gotowy do nauki asyncio!".
# Uruchom ją za pomocą asyncio.run()

import asyncio

async def start():
    print("Gotowy do nauki asyncio!")

asyncio.run(start())