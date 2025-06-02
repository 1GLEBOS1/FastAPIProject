from typing import Optional
from db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from bcrypt import hashpw, gensalt

def hashed(s: str) -> str:
    return hashpw(s.encode('utf-8'), gensalt()).decode('utf-8')

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)

def create_user(db: Session, name: str, email: str, password: str):

    user = Users(name=name, email=email, hash_password=hashed(password))
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_user_by_email(db: Session, email: str):
    return db.query(Users).filter(Users.email == email).first()

def update_user(db: Session, user: Users, name: Optional[str], email: Optional[str], password: Optional[str]):
    if name is not None:
        user.name = name
    if email is not None:
        user.email = email
    if password is not None:
        user.hash_password = hashed(password)
    db.update(user)
    db.commit()
    db.refresh(user)
    return user

def read_user(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()

def delete_user(db: Session, user: Users):
    db.delete(user)
    db.commit()
    return None
