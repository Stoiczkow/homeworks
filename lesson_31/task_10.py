# Współbieżne odliczanie
# Napisz korutynę odliczanie(nazwa, start), która co sekundę drukuje komunikat "{nazwa}:
# zostało {pozostało} sekund". Uruchom trzy takie odliczania współbieżnie, każde z inną
# nazwą i innym czasem początkowym (np. 5s, 3s, 7s)

import asyncio, random

async def odliczanie(counter_nr, start):
    for i in range(start, 0, -1):
        print(f"Odliczanie {counter_nr}: Zostało {i} sekund")
        await asyncio.sleep(1)
        
async def main():
    tasks = [
        odliczanie(counter_nr, random.randint(3,10)) for counter_nr in range(1,4)     
    ]
    await asyncio.gather(*tasks)
    
asyncio.run(main())