# Łańcuch zależności
# Stwórz łańcuch zależnych od siebie korutyn:
# 1. pobierz_id_uzytkownika(nazwa_uzytkownika) -> zwraca ID po 1s.
# 2. pobierz_posty(id_uzytkownika) -> zwraca listę ID postów po 1s.
# 3. pobierz_komentarze(id_postu) -> zwraca listę komentarzy po 1s.
# Napisz main, które dla nazwy użytkownika pobierze jego ID, następnie listę jego
# postów, a na końcu pobierze komentarze dla wszystkich jego postów współbieżnie.
# Zmierz czas wykonania.
import asyncio, random, time

async def get_user_id(username):
    print(f"Pobieranie id uzytkownika o nazwie: {username}...")
    id = random.randint(1, 1000)
    await asyncio.sleep(1)
    print(f"Pobrano id uzytkownika o nazwie: {username}")
    
    return id

async def get_posts(user_id):
    print(f"Pobieranie postów uzytkownika o id: {user_id}...")
    posts = [
        {id: 1, 'nazwa': 'post1'}, 
        {id: 2, 'nazwa': 'post2'}, 
        {id: 3, 'nazwa': 'post3'}
        ]
    await asyncio.sleep(1)
    print(f"Posty uzytkownika o id: {user_id} pobrane!")
    
    return posts

async def get_comments(post_id):
    print(f"Pobieranie komantarzy do postu o id: {post_id}...")
    comments = ['komentarz1', 'komentarz2', 'komentarz3']
    await asyncio.sleep(1)
    print(f"Komentarze do postu o id: {post_id} pobrane!")
    return comments

async def main():
    start_time = time.time()
    
    user_id = await get_user_id('Hania')
    posts = await get_posts(user_id)
    
    comments_to_all_posts = [
        get_comments(post.id for post in posts)
    ]
    
    all_comments = await asyncio.gather(*comments_to_all_posts)
    
    print(f"Wszytskie komentarze to: {all_comments}")
    
    end_time = time.time()
    
    print(f"Całkowity czas wykonania: {end_time - start_time:.2f}s")
    
asyncio.run(main())