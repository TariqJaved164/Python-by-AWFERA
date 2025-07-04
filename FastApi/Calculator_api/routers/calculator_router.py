from fastapi import APIRouter, HTTPException

# Create a new APIRouter instance
calculator_router = APIRouter()


@calculator_router.get("/add" , summary = "Add two numbers")
def add_numbers(x:float, y:float):
   
    """
    Return the sum of two numbers
    """
    return {"operation" : "Addition", "x": x, "y": y, "Result": x + y}


@calculator_router.get("/subtract" , summary = "Subtract  two numbers")
def add_numbers(x:float, y:float):
   
    """
    Return the difference of two numbers
    """
    return {"operation" : "Subtraction", "x": x, "y": y, "Result": x - y}


@calculator_router.get("/Multiply" , summary = "Multiply two numbers")
def add_numbers(x:float, y:float):
   
    """
    Return the Product of two numbers
    """
    return {"operation" : "Multiplication", "x": x, "y": y, "Result": x * y}


@calculator_router.get("/divide" , summary = "Divide  two numbers with error handling")
def add_numbers(x:float, y:float):
   
    """
    Returns the quotient of x divided by y.
    Raises an error if division by zero is attempted.
    """
    if y == 0:
        raise HTTPException(status_code = 400, detail = "Division by is not allowed")
                            
    return {"operation" : "Division", "x": x, "y": y, "Result": x / y}