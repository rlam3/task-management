from datetime import datetime, UTC
from typing import List
from . import models
from sqlalchemy.orm import Session


class TaskRepository:
    def __init__(self, db: Session = None):
        self.db = db
        self._tasks = []
        self._current_id = 1

    def create(self, description: str) -> models.Task:
        if self.db:
            task = models.Task(description=description)
            self.db.add(task)
            self.db.commit()
            self.db.refresh(task)
            return task

        # For testing without database
        task = models.Task(
            id=self._current_id, description=description, created_at=datetime.now(UTC)
        )
        self._tasks.append(task)
        self._current_id += 1
        return task

    def get_all(self) -> List[models.Task]:
        if self.db:
            return self.db.query(models.Task).all()
        return self._tasks
