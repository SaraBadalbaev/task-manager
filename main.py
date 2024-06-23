# Run the app with: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List, Literal
import uuid
from models import Task, TaskManager  # Import the Task and TaskManager models
from firebase_config import db  # Import Firebase configuration
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
task_manager = TaskManager()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
   
    task.id = str(uuid.uuid4())
    task_manager.tasks.append(task)
    db.collection("tasks").document(task.id).set(task.dict())
    return task

@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    tasks = [Task(**task.to_dict()) for task in db.collection("tasks").stream()]
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: str):
    
    task_ref = db.collection("tasks").document(task_id)
    task = task_ref.get()
    if task.exists:
        return task.to_dict()
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, task: Task):
    task_ref = db.collection("tasks").document(task_id)
    task_ref.update(task.dict(exclude_unset=True))
    updated_task = task_ref.get()
    if updated_task.exists:
        return updated_task.to_dict()
    else:
        raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    
    task_ref = db.collection("tasks").document(task_id)
    task_ref.delete()
    return {"message": "Task deleted successfully"}

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    tasks = [task.to_dict() for task in db.collection("tasks").stream()]
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.get("/tasks/priority/{priority}", response_model=List[Task])
async def read_tasks_by_priority(priority:Literal["low", "medium", "high"]):
    tasks = [task.to_dict() for task in db.collection("tasks").where("priority", "==", priority).stream()]
    return tasks
   
@app.get("/tasks/label/{label}", response_model=List[Task])
async def read_tasks_by_label(label: str):
    tasks = [task.to_dict() for task in db.collection("tasks").where("label", "==", label).stream()]
    return tasks

@app.get("/tasks/search/", response_model=List[Task])
async def search_tasks(query: str = Query(None, min_length=1)):
    # Filter tasks based on the search query (search in title or description)
    filtered_tasks = [
        task.to_dict() for task in task_manager.tasks
        if query.lower() in task.title.lower() or (task.description and query.lower() in task.description.lower())
    ]
    return filtered_tasks







