from fastapi import FastAPI
from routers.calculator_router import calculator_router


# Create a FastAPI intance
app = FastAPI(
    title = "Calculator API",
    description = "A simple calculator API to perform basic arithmetic operations",
    version = "1.0.0"
    )

# Include the calculator router
app.include_router(calculator_router, prefix = "/calculator", tags = ["Calculator"])
 