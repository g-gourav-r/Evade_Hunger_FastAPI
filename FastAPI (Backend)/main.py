import hashlib
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.sqlite import engine, SessionLocal
from app.crud import user_crud
from app.models.user import UserCreate, User


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to create a new user
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)