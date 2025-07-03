# import BaseModel from pydantic to define data model
from pydantic import BaseModel

# define the structure of todo items
class ToDoItem(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
    