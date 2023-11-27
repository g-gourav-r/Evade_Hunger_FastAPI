This is a simple FastAPI backend for managing donations and users.

## Overview

The application is designed to handle two main functionalities: donation management and user management. It provides RESTful APIs for adding food items for donation, updating their status, and managing user information.

## Project Structure

The project follows a modular structure for better organization:

* `app/`: The main package for the FastAPI application.
  * `donation/`: Module for donation-related components.
    * `models.py`: Pydantic models for donation.
    * `routes.py`: FastAPI routes for donation.
    * `services.py`: Functions handling business logic for donation.
  * `users/`: Module for user-related components.
    * `models.py`: Pydantic models for users.
    * `routes.py`: FastAPI routes for users.
    * `services.py`: Functions handling business logic for users.
  * `main.py`: Main file to initialize the FastAPI app and include routes


## Usage

1. Run the FastAPI application:

   ```uvicorn app.main:app --reload ```

   The application will be available at `http://127.0.0.1:8000`.
2. Access the Swagger UI for API documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
3. Access the ReDoc for an alternative documentation view: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

## API Documentation

The API documentation is generated dynamically from the code docstrings. You can explore and test the APIs using the Swagger UI or ReDoc interfaces.

* **Donation Endpoints:**
  * Add Food: `/add_food/`
  * Update Food Status: `/update_food_status`
  * View All Food: `/view_all_food/`
  * View Food with Status: `/view_food_with_status/{status}`
* **User Endpoints:**
  * Add User: `/add_user`
  * View All Users: `/users`
  * Update User Type: `/update_user_type`
