# Import FastAPI class from fastapi module
from fastapi import FastAPI

# Create an instance of the FastAPI application
application = FastAPI()

# Root endpoint to verify the API is running
@application.get("/")
def read_homepage():
    # Return a welcome message in JSON format
    return {"message": "Welcome to your first FastAPI application!"}

# Custom endpoint to greet a user by name
@application.get("/greet/{user_name}")
def greet_user(user_name: str):
    # Return a personalized greeting
    return {"greeting": f"Hello, {user_name}! Nice to meet you."}

# Custom endpoint to add two numbers provided as query parameters
@application.get("/add")
def add_two_numbers(first_number: int, second_number: int):
    # Calculate the sum of two numbers
    result = first_number + second_number
    # Return the result
    return {"result": result}

# Custom endpoint to simulate stopping the application (for demonstration)
@application.get("/stop")
def stop_application():
    # Simulated response; actual server stop requires process management
    return {"status": "Application would stop here (simulation)."}
