from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from datetime import datetime, UTC
from typing import List


app = FastAPI(title="Task Management API")


class TaskCreate(BaseModel):
    description: str


class Task(TaskCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime


# In-memory storage for tasks
tasks = []
current_id = 1


@app.post("/tasks/", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    """Create a new task."""
    global current_id
    new_task = Task(
        id=current_id, description=task.description, created_at=datetime.now(UTC)
    )
    tasks.append(new_task)
    current_id += 1
    return new_task


@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    """Get all tasks."""
    return tasks
