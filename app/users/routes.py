from fastapi import APIRouter
from .models import UserCreate, UserTypeUpdate
from .services import add_user, show_users, update_user_type

router = APIRouter()


@router.post("/add_user")
async def add_user_route(user: UserCreate):
    return add_user(user)


@router.get("/users")
def show_users_route():
    return show_users()


@router.put("/update_user_type")
async def update_user_type_route(user_data: UserTypeUpdate):
    return update_user_type(user_data)
