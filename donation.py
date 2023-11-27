from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Define Pydantic models for request and response
class FoodItem(BaseModel):
    name: str
    quantity: int
    location: str

class FoodUpdate(BaseModel):
    ID: int
    status: bool
    name: str
    password: str


def get_database_connection():
    return sqlite3.connect("database.db")

@app.post("/add_food/", response_model=dict)
async def add_food(food_item: FoodItem):
    # Establish a new connection to the database
    conn = get_database_connection()
    cursor = conn.cursor()

    try:
        # Add a new entry to the food table with status=0 by default
        cursor.execute(
            "INSERT INTO food (name, quantity, location, status) VALUES (?, ?, ?, ?)",
            (food_item.name, food_item.quantity, food_item.location, 0),
        )
        conn.commit()
        return {"message": "Food entry added successfully"}
    finally:
        # Close the database connection
        conn.close()


# FastAPI endpoint to handle the update

@app.put("/update_food_status")
async def update_food_status(food_data: FoodUpdate):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM users WHERE name = ? AND password = ?"
        cursor.execute(query, (food_data.name, food_data.password))
        user = cursor.fetchone()

        # Check if user has proper access (assuming the access level is in user[3])
        if user and user[3] not in (1, 2):
            return {"message": "Access denied"}

        # Authenticate user
        if not user:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        # Check if the food_id exists in the database
        check_query = "SELECT * FROM food WHERE ID = ?"
        cursor.execute(check_query, (food_data.ID,))
        existing_food = cursor.fetchone()

        if not existing_food:
            raise HTTPException(status_code=400, detail="Invalid operation. Choose a valid food_id.")

        # Update food status
        update_query = "UPDATE food SET status = ? WHERE ID = ?"
        cursor.execute(update_query, (food_data.status, food_data.ID))

        return {"message": f"Food status updated successfully for food_id: {food_data.ID}"}
    finally:
        conn.close()


@app.get("/view_all_food/", response_model=list)
async def view_all_food():
    # Establish a new connection to the database
    conn = get_database_connection()
    cursor = conn.cursor()

    try:
        # Fetch all entries from the food table
        cursor.execute("SELECT * FROM food")
        entries = cursor.fetchall()
        return entries
    finally:
        # Close the database connection
        conn.close()


@app.get("/view_food_with_status/{status}", response_model=list)
async def view_food_with_status(status: int):
    # Establish a new connection to the database
    conn = get_database_connection()
    cursor = conn.cursor()

    try:
        # Fetch entries from the food table with the specified status
        cursor.execute("SELECT * FROM food WHERE status = ?", (status,))
        entries = cursor.fetchall()
        return entries
    finally:
        # Close the database connection
        conn.close()
