from fastapi import FastAPI, HTTPException
from models import Todo

app = FastAPI()

@app.get("/")
async def root():
    return { "message" : "Hello World" }

todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return { "todos" : todos }

# Get single todo
@app.get("/todos/{todo_id}")
async def get_todos(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return { "todo": todo }
    return { "message" : "Todo not found" }

# Create a todo
@app.post("/todos")
async def get_todos(todo: Todo):
    todos.append(todo)
    return { "message" : "Todo has been added" }

# Update a todo
@app.put("/todos/{todo_id}")
async def get_todos(todo_id: int, todo_update: Todo):
    if not any(todo.id == todo_id for todo in todos):
        raise HTTPException(status_code=404, detail="Item not found")

    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_update.id
            todo.item = todo_update.item
            todo.title = todo_update.title

    return { "message" : "Todo has been updated" }

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    if not any(todo.id == todo_id for todo in todos):
        raise HTTPException(status_code=404, detail="Item not found")

    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
    return { "message" : "Todo has been removed" }