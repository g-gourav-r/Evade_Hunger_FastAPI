from fastapi import APIRouter
from .models import FoodUpdate
from .models import FoodItem
from .services import add_food, update_food_status, view_all_food, view_food_with_status

router = APIRouter()


@router.post("/add_food/", response_model=dict)
async def add_food_route(food_item: FoodItem):
    return await add_food(food_item)


@router.put("/update_food_status")
async def update_food_status_route(food_data: FoodUpdate):
    return await update_food_status(food_data)


@router.get("/view_all_food/", response_model=list)
async def view_all_food_route():
    return await view_all_food()


@router.get("/view_food_with_status/{status}", response_model=list)
async def view_food_with_status_route(status: int):
    return await view_food_with_status(status)
