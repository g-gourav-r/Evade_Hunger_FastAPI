from pydantic import BaseModel


class FoodItem(BaseModel):
    name: str
    quantity: int
    location: str


class FoodUpdate(BaseModel):
    ID: int
    status: bool
    name: str
    password: str
