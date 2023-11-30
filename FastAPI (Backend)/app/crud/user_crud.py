# app/crud/user_crud.py

from sqlalchemy.orm import Session
from app.models.user import UserCreate
import hashlib

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(**user.dict(), password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def hash_password(password: str):
    password_bytes = password.encode('UTF-8')
    hash_object = hashlib.sha256(password_bytes)
    hex_digest = hash_object.hexdigest()
    return hex_digest
