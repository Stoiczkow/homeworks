#  Zadanie 4 – GraphQL - Query użytkownika
# Stwórz prosty GraphQL API z typem User(id, name, email) i query user(id: ID!)
# zwracającym użytkownika z fake listy

#  Zadanie 5 – GraphQL - Lista użytkowników
# Rozszerz API z zadania 4 o query users zwracające listę wszystkich użytkowników

# Zadanie 6 – GraphQL Mutation
# Dodaj mutację createUser(name: String!, email: String!) która dodaje użytkownika
# do listy i zwraca go

# Zadanie 10 – GraphQL z relacjami
# Stwórz API z typami User i Post , gdzie User ma pole posts zwracające listę jego
# postów, oraz Post ma pole author zwracające autora.

# Zadanie 12 – GraphQL z filtrowaniem
# Rozszerz API z zadania 10 o query posts(authorId: ID) filtrujące posty po autorze oraz
# searchUsers(name: String) wyszukujące użytkowników

import strawberry

from typing import List, Optional
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView

@strawberry.type
class Post:
    id: int
    title: str
    content: str
    author_id: int

    @strawberry.field
    def author(self) -> Optional["User"]:
        for user in fake_users_db:
            if user.id == self.author_id:
                return user
        return None
    
@strawberry.type
class User:
    id: int
    name: str
    email: str
    
    @strawberry.field
    def posts(self) -> List[Post]:
        return [
            post for post in fake_posts_db 
            if post.author_id == self.id
        ]


fake_users_db = [
    User(id=1, name="Jan Kowalski", email="jan@example.com"),
    User(id=2, name="Anna Nowak", email="anna@example.com")
]

fake_posts_db = [
    Post(id=1, title="Python jest super", content="...", author_id=1),
    Post(id=2, title="GraphQL tutorial", content="...", author_id=1),
    Post(id=3, title="Asynchroniczność", content="...", author_id=2),
]

@strawberry.type
class Query:

    @strawberry.field
    def user(self, id: int) -> Optional[User]:

        for user in fake_users_db:
            if user.id == id:
                return user

        return None
    
    @strawberry.field
    def users(self) -> List[User]:

        return fake_users_db
    
    @strawberry.field
    def posts(self, author_id: int) -> List[Post]:
        return [
            post for post in fake_posts_db
            if post.author_id == author_id
        ]
        
    @strawberry.field 
    def search_users(self, name: str) -> List[User]:
        return [
            user for user in fake_users_db
            if name.lower() in user.name.lower()
        ]

@strawberry.type
class Mutation:
    
    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        new_id = max((u.id for u in fake_users_db), default=0) + 1
        new_user = User(id=new_id, name=name, email=email)
        fake_users_db.append(new_user)
        return new_user
        
        
schema = strawberry.Schema(query=Query, mutation=Mutation)

app = web.Application()

app.router.add_route(
    "*",
    "/graphql",
    GraphQLView(schema=schema)
)


if __name__ == "__main__":
    print("🚀 GraphQL API działa na http://localhost:8000/graphql")
    web.run_app(app, host="localhost", port=8000)