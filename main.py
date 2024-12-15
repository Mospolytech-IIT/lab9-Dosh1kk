"main"
from sqlalchemy.orm import DeclarativeBase
from fastapi import FastAPI
from functions import add_user, add_post, get_all_users, get_all_posts, update_user_email
from functions import update_post_content, delete_post, delete_user_and_posts

#базовый класс
class Base(DeclarativeBase): pass

#Base.metadata.create_all(bind=engine)

app=FastAPI()


@app.get("/users/")
def read_users():
    "получение пользователей"
    return get_all_users()

@app.get("/posts/")
def read_posts():
    "получение постов"
    return get_all_posts()

@app.post("/users/")
def create_user(username,email,password):
    "добавление пользователей"
    add_user(username, email, password)

@app.post("/posts/")
def create_post(title,content,user_id):
    "добавление постов"
    add_post(title, content, user_id)

@app.put("/users/{user_id}")
def update_user(user_id: int, email: str):
    "изменение пользователей"
    update_user_email(user_id, email)

@app.put("/posts/{post_id}")
def update_post(post_id: int, content: str):
    "изменение постов"
    update_post_content(post_id, content)

@app.delete("/posts/{post_id}")
def remove_post(post_id: int):
    "удаление пользователей"
    delete_post(post_id)

@app.delete("/users/{user_id}")
def remove_user(user_id: int):
    "удаление постов"
    delete_user_and_posts(user_id)
