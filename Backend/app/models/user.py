# app/models/user.py

from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str  # This will be the plain text password

class UserCreate(User):
    pass