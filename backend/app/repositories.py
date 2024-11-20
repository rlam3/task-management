from datetime import UTC, datetime

from sqlalchemy.orm import Session

from . import models


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

        task = models.Task(
            id=self._current_id, description=description, created_at=datetime.now(UTC)
        )
        self._tasks.append(task)
        self._current_id += 1
        return task

    def get_all(self) -> list[models.Task]:
        if self.db:
            return self.db.query(models.Task).all()
        return self._tasks

    def delete(self, task_id: int) -> bool:
        if self.db:
            task = self.db.query(models.Task).filter(models.Task.id == task_id).first()
            if task:
                self.db.delete(task)
                self.db.commit()
                return True
            return False

        task_idx = next(
            (idx for idx, task in enumerate(self._tasks) if task.id == task_id), None
        )
        if task_idx is not None:
            self._tasks.pop(task_idx)
            return True
        return False
