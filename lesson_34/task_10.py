# 10. ✏ Zadanie 10 – GraphQL z relacjami
# Stwórz API z typami User i Post , gdzie User ma pole posts zwracające listę jego
# postów, oraz Post ma pole author zwracające autora.
# (średnie)


import strawberry
from typing import List, Optional
from aiohttp import web
from strawberry.aiohttp.views import GraphQLView


@strawberry.type
class Post:
    """Typ reprezentujący post w blogu"""

    id: int
    title: str
    content: str
    author_id: int

    @strawberry.field
    def author(self) -> "User":
        for user in fake_users_db:
            if user.id == self.author_id:
                return user


@strawberry.type
class User:
    """Typ reprezentujący użytkownika"""

    id: int
    name: str
    email: str

    @strawberry.field
    def posts(self) -> List[Post]:
        return [post for post in fake_posts_db if post.author_id == self.id]


fake_users_db = [
    User(id=1, name="Jan Kowalski", email="jan@example.com"),
    User(id=2, name="Anna Nowak", email="anna@example.com"),
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
        """Pobierz użytkownika po ID"""
        for user in fake_users_db:
            if user.id == id:
                return user
        return None

    @strawberry.field
    def users(self) -> List[User]:
        """Pobierz wszystkich użytkowników"""
        return fake_users_db

    @strawberry.field
    def post(self, id: int) -> Optional[Post]:
        """Pobierz post po ID"""
        for post in fake_posts_db:
            if post.id == id:
                return post
        return None


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_user(self, name: str, email: str) -> User:
        """Utwórz nowego użytkownika"""
        new_id = max([u.id for u in fake_users_db]) + 1
        new_user = User(id=new_id, name=name, email=email)
        fake_users_db.append(new_user)
        return new_user


schema = strawberry.Schema(query=Query, mutation=Mutation)

app = web.Application()

# GraphQL endpoint z interfejsem GraphiQL (do testowania)
app.router.add_route("*", "/graphql", GraphQLView(schema=schema))

if __name__ == "__main__":
    print("🚀 GraphQL API działa na http://localhost:8000/graphql")
    print("📊 Otwórz w przeglądarce, aby użyć GraphiQL interface")
    web.run_app(app, host="localhost", port=8000)