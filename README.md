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

```
