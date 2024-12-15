"functions file"
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import  Column, Integer, String,Text
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://postgres:Dasha2004!@localhost:5432/database1')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase): pass


class User(Base):
    "Пользователь"
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    posts = relationship("Post", back_populates="user")

class Post(Base):
    "Пост"
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="posts")

def add_user(username, email, password):
    "добавление пользователя"
    session = SessionLocal()
    new_user = User(username=username, email=email, password=password)
    session.add(new_user)
    session.commit()
    session.close()

def add_post(title, content, user_id):
    "добавление поста"
    session = SessionLocal()
    new_post = Post(title=title, content=content, user_id=user_id)
    session.add(new_post)
    session.commit()
    session.close()

def delete_post(post_id):
    "удаление поста"
    session = SessionLocal()
    post = session.query(Post).filter(Post.id == post_id).first()
    if post:
        session.delete(post)
        session.commit()
    session.close()

def delete_user_and_posts(user_id):
    "удаление ползователя"
    session = SessionLocal()
    posts = session.query(Post).filter(Post.user_id == user_id).all()
    for post in posts:
        session.delete(post)
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()

def update_user_email(user_id, new_email):
    "изменение почты пользователя"
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        user.email = new_email
        session.commit()
    session.close()

def update_post_content(post_id, new_content):
    "Изменение контента поста"
    session = SessionLocal()
    post = session.query(Post).filter(Post.id == post_id).first()
    if post:
        post.content = new_content
        session.commit()
    session.close()

def get_all_users():
    "получение всех пользователей"
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return users

def get_all_posts():
    "получение всех постов"
    session = SessionLocal()
    posts = session.query(Post).all()
    session.close()
    return posts

def get_posts_by_user(user_id):
    "получение постов определенного пользователя"
    session = SessionLocal()
    posts = session.query(Post).filter(Post.user_id == user_id).all()
    session.close()
    return posts
