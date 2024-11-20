from fastapi.testclient import TestClient
import pytest
from app.main import app, get_repository
from app.repositories import TaskRepository

client = TestClient(app)


@pytest.fixture(autouse=True)
def mock_repo():
    """Provide test repository and override dependency."""
    repo = TaskRepository()
    app.dependency_overrides[get_repository] = lambda: repo
    yield
    app.dependency_overrides.clear()


class TestCreateTask:
    def test_returns_201_when_creating_task(self):
        """Test successful task creation returns 201."""
        response = client.post("/tasks/", json={"description": "Test task"})
        assert response.status_code == 201

    def test_creates_task_with_correct_description(self):
        """Test created task has correct description."""
        description = "Complete TDD implementation"
        response = client.post("/tasks/", json={"description": description})
        created_task = response.json()
        assert created_task["description"] == description

    def test_returns_422_when_description_missing(self):
        """Test validation when required field is missing."""
        response = client.post("/tasks/", json={})
        assert response.status_code == 422


class TestGetTasks:
    def test_returns_200_when_getting_tasks(self):
        """Test get tasks returns 200 status."""
        response = client.get("/tasks/")
        assert response.status_code == 200

    def test_returns_empty_list_initially(self):
        """Test get tasks returns empty list when no tasks exist."""
        response = client.get("/tasks/")
        assert response.json() == []

    def test_returns_task_after_creation(self):
        """Test get tasks returns task after it's created."""
        description = "New task"
        client.post("/tasks/", json={"description": description})

        response = client.get("/tasks/")
        tasks = response.json()
        assert any(task["description"] == description for task in tasks)


class TestDeleteTask:
    def test_returns_204_when_task_deleted(self):
        """Test successful task deletion returns 204."""
        # Create a task
        create_response = client.post("/tasks/", json={"description": "Task to delete"})
        task_id = create_response.json()["id"]

        # Delete the task
        response = client.delete(f"/tasks/{task_id}")
        assert response.status_code == 204

    def test_returns_404_when_deleting_nonexistent_task(self):
        """Test deleting non-existent task returns 404."""
        response = client.delete("/tasks/999")
        assert response.status_code == 404

    def test_deleted_task_not_in_list(self):
        """Test deleted task is removed from tasks list."""
        # Create a task
        create_response = client.post("/tasks/", json={"description": "Task to delete"})
        task_id = create_response.json()["id"]

        # Delete the task
        client.delete(f"/tasks/{task_id}")

        # Verify task is not in list
        response = client.get("/tasks/")
        tasks = response.json()
        assert not any(task["id"] == task_id for task in tasks)
