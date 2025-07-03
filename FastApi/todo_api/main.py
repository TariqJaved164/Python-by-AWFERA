from fastapi import FastAPI
from routers.todo_routers import todo_router



# Creating an instance of FastAPI
app = FastAPI(  
    title = "Todo List API",
    description = "A siple ApI for managing a todo list",
    version = "1.0.0"
)

# including the routers
app.include_router(
    todo_router,
    prefix = "/todos",
    tags = ["todos"]
)