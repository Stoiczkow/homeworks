from fastapi import FastAPI, HTTPException, status, Depends, BackgroundTasks, Request, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from ai_agent import generate_response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError
from database import get_db, init_db, AsyncSessionLocal, engine
from models import UsersORM, PostORM, CommentORM, SummaryORM

import aiofiles
import json

from datetime import datetime
from faker import Faker
from typing import List

from schemas import (
    UserBase, UserCreate,
    PostCreate, PostBase, PostUpdate,
    CommentBase, CommentWithId, SummaryBase
    )

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    print("Database initialized!")

    yield

    print("Application is shutting down...")

    await engine.dispose()
    print("Database connections closed!")

app = FastAPI(lifespan=lifespan)

### BACKGROUND TASKS ###

async def email_log(message: str):
    async with aiofiles.open("email.log", "a", encoding="UTF-8") as f:
        timestamp = datetime.now().isoformat()
        await f.write(f"{timestamp} - {message}\n")

async def comment_sentiment_analyze(message: str, comment_id: int):
    async with AsyncSessionLocal() as db:
        try:
            llm_response = await generate_response(f"Please analyze this comment's sentiment: {message}, return only text from selected values (one word): positive, neutral, negative")
            sentiment = llm_response.strip().lower()
        
            if sentiment not in ['positive', 'neutral', 'negative']:
                sentiment = 'notset'

            query = update(CommentORM).where(CommentORM.id == comment_id).values(sentiment=sentiment)
            await db.execute(query)
            await db.commit()

        except Exception as e:
            print(f"[Background Task Error] Analiza sentymentu nie powiodła się: {e}")
            await db.rollback()

### MIDDLEWARE ###

@app.middleware("http")
async def check_if_vulgar(request: Request, call_next):

    if request.method == "POST":
        try:
            body = await request.body()

            if body:
                json_data = json.loads(body)
                try:
                    evaluation = await generate_response(f"Check if this message has any vulgar profanities: {json_data} if so, return 'yes', if not 'no' (just one word and nothing else)")
                    evaluation = evaluation.strip().lower()
                except Exception:
                    evaluation = "no"
                
                if "yes" in evaluation:
                    return JSONResponse(
                        status_code=422,
                        content={"detail": "Please avoid profanity"}
                    )
                

                async def receive():
                    return {"type": "http.request", "body": body}
                
                request._receive = receive

        except Exception as e:
                    print(f"[Middleware Error] {e}")

    response = await call_next(request)
    return response


### USERS ENDPOINT ###

@app.get("/users", status_code=200)
async def get_users(db: AsyncSession = Depends(get_db)):
    
    query = select(UsersORM)

    result = await db.execute(query)
    users = result.scalars().all()
    
    if not users:
        raise HTTPException(status_code=404,
                            detail="Empty response")

    return users


@app.post("/users", status_code=201)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        db_user = UsersORM(**user.model_dump())
        db.add(db_user)
        await db.commit()
    except IntegrityError:
        raise HTTPException(status_code=400,
                            detail="Couldn't save book in the database. Make sure you've chosen distinct name")
    
    await db.refresh(db_user)

    return db_user

@app.delete("/users/{id}", status_code=200)
async def delete_user(id: int, db: AsyncSession = Depends(get_db)):

    query = await db.execute(select(UsersORM).where(UsersORM.id == id))

    user = query.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=404,
                            detail="User with that ID does not exist")
    
    await db.delete(user)
    await db.commit()

    return {"message": f"User with {user.id} deleted"}


@app.patch("/users/{id}", status_code=200, response_model=UserBase)
async def update_user(id: int, user_update: UserCreate, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(UsersORM).where(UsersORM.id == id))
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=404,
                            detail="Book with that ID does not exist")
    
    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(user, field, value)

    await db.commit()

    return user

### POST ENDPOINTS ###

@app.get("/posts", status_code=200)
async def get_posts(db: AsyncSession = Depends(get_db)):
    
    query = select(PostORM)

    result = await db.execute(query)
    posts = result.scalars().all()
    
    if not posts:
        raise HTTPException(status_code=404,
                            detail="Empty response")
    
    return posts


@app.post("/posts", status_code=201, response_model=PostBase)
async def create_user(post: PostCreate, db: AsyncSession = Depends(get_db)):
    db_post = PostORM(**post.model_dump())
    query = await db.execute(select(UsersORM).where(UsersORM.id == db_post.author_id))
    user_exists = query.scalar_one_or_none()
    if user_exists:
        db.add(db_post)
        await db.commit()
        return db_post
    else:
        raise HTTPException(status_code=400,
                            detail="Invalid User")

@app.delete("/posts/{id}", status_code=200)
async def delete_post(id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(PostORM).where(PostORM.id == id))
    post = result.scalar_one_or_none()
    
    if not post:
        raise HTTPException(status_code=404,
                            detail="Post with that ID does not exist")

    await db.delete(post)
    await db.commit()

    return {"info": f"Post {id} deleted"}


@app.patch("/posts/{id}", status_code=200, response_model=PostBase)
async def update_post(id: int, post_update: PostUpdate, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(PostORM).where(PostORM.id == id))
    post = result.scalar_one_or_none()

    user_query = await db.execute(select(UsersORM).where(UsersORM.id == post_update.author_id))
    user_exists = user_query.scalar_one_or_none()

    if not user_exists:
        raise HTTPException(status_code=400,
                            detail="Invalid user")
    
    if not post:
        raise HTTPException(status_code=404,
                            detail="Post with that ID does not exist")
    
    update_data = post_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(post, field, value)

    await db.commit()

    return post

@app.get("/posts/{id}/with-comments", status_code=200)
async def get_posts(id: int, db: AsyncSession = Depends(get_db)):
    
    query = select(PostORM).where(PostORM.id == id).options(selectinload(PostORM.comments))

    result = await db.execute(query)
    posts = result.scalars().all()
    
    if not posts:
        raise HTTPException(status_code=404,
                            detail="Empty response")
    return posts


@app.post("/posts/{id}/summarize", status_code=200)
async def llm_summarize(id: int, db: AsyncSession = Depends(get_db)):
    
    query = select(PostORM).where(PostORM.id == id)

    result = await db.execute(query)
    post = result.scalar_one_or_none()
    
    if not post:
        raise HTTPException(status_code=404,
                            detail="Given post does not exist")
    
    original_content = post.content
    try:
        summary_text = await generate_response(f"Please summarize this blog post: {original_content}, return only text of that summary")
    except Exception:
        raise HTTPException(status_code=502,
                        detail="No correct response from LLM model")
    db_summary = SummaryORM(content=summary_text,
                            post_id=id)

    db.add(db_summary)
    await db.commit()
    
    return db_summary

### COMMENTS ###


@app.post("/comments", status_code=201, response_model=CommentWithId)
async def create_comment(background_tasks: BackgroundTasks, post: CommentBase, db: AsyncSession = Depends(get_db)):

    db_comment = CommentORM(**post.model_dump())
    query = await db.execute(select(PostORM).where(PostORM.id == db_comment.post_id))
    post_exists = query.scalar_one_or_none()
    if post_exists:
        db.add(db_comment)
        await db.commit()
        
        background_tasks.add_task(
            email_log,
            f"Nowy komentarz dla posta {post_exists.id}!"
            )
        
        background_tasks.add_task(
            comment_sentiment_analyze,
            message = db_comment.content,
            comment_id = db_comment.id
            )
        
        return db_comment

    else:
        raise HTTPException(status_code=400,
                            detail="Given post does not exists")