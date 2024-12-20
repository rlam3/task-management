from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

from .database import get_db
from .repositories import TaskRepository

app = FastAPI(title="Task Management API")

# More permissive CORS settings for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,  # Changed since we're not using credentials
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


def get_repository(db: Session = Depends(get_db)) -> TaskRepository:
    return TaskRepository(db)


class TaskCreate(BaseModel):
    description: str


class Task(TaskCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime


@app.post("/tasks/", response_model=Task, status_code=201)
async def create_task(task: TaskCreate, repo: TaskRepository = Depends(get_repository)):
    """Create a new task."""
    return repo.create(task.description)


@app.get("/tasks/", response_model=list[Task])
async def get_tasks(repo: TaskRepository = Depends(get_repository)):
    """Get all tasks."""
    return repo.get_all()


@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int, repo: TaskRepository = Depends(get_repository)):
    """Delete a task."""
    if not repo.delete(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
