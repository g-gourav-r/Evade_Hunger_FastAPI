from fastapi import FastAPI

app = FastAPI()

# Include routes from submodules
from app.donation import routes as donation_routes
from app.users import routes as users_routes

app.include_router(donation_routes.router)
app.include_router(users_routes.router)

