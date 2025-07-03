# import APIRouter for modular routing
from fastapi import APIRouter , HTTPException
from typing import List
from models.todo_model import ToDoItem


# Create router intance.
todo_router = APIRouter()

# In-memory list to store todo items.
todo_items: list[ToDoItem] = []


@todo_router.post("/", response_model=ToDoItem,summary="Create a new todo item")
def create_todo_item(todo_item:ToDoItem):
    """
    Add a new todo item with unique ID ,title and description.
    """
    todo_items.append(todo_item)
    return todo_item

@todo_router.get("/", response_model=List[ToDoItem], summary="Get all todo items")
def get_todo_items():
    
    """
    Retrieve all todo items.
    """
    return todo_items

@todo_router.put("/{todo_id}/complete", response_model=ToDoItem, summary="Mark a todo item as complete")
def complete_todo_item(todo_id:int):
    """
    Mark a todo item as complete by its ID.
    """
    for item in todo_items:
        if item.id == todo_id:
            item.completed = True
            return item
    raise HTTPException(status_code=404, detail="Todo item not found")


@todo_router.delete("/{todo_id}", summary="Delete a todo item")
def delete_todo(todo_id: int):
    """
    Delete a todo item from the list by its ID.
    """
    for index, item in enumerate(todo_items):
        if item.id == todo_id:
            del todo_items[index]
            return {"message": "Todo item deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo item not found")


    