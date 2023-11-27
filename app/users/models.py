from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    password: str
    email: str
    phone: str


class UserTypeUpdate(BaseModel):
    user_id: int
    username: str
    password: str
    new_type: int
