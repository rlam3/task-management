# Task Management Application

A full-stack task management application built with FastAPI, PostgreSQL, and Vue.js.

## Features

- Create and view tasks
- Real-time updates
- Clean, responsive UI
- Database persistence

## Tech Stack

### Frontend

- Vue.js 3 with TypeScript
- Tailwind CSS for styling
- Vite for development
- Unit tests with Vitest

### Backend

- FastAPI
- PostgreSQL database
- SQLAlchemy ORM
- Repository pattern
- Unit tests with pytest

## Development Setup

### Database Setup

1. Install PostgreSQL if not already installed:

```bash
# macOS (using Homebrew)
brew install postgresql
brew services start postgresql
```

2. Create the database:

```bash
createdb task_management
```

3. Update database connection (if needed):
   - Open `backend/app/database.py`
   - Modify `SQLALCHEMY_DATABASE_URL` if your PostgreSQL credentials are different:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/task_management"
```

### Backend Setup

1. Install Poetry if not already installed:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies and activate virtual environment:

```bash
cd backend
poetry install
poetry shell
```

3. Run the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at <http://localhost:8000>

### Frontend Setup

1. Install dependencies:

```bash
cd frontend
npm install
```

2. Run the development server:

```bash
npm run dev
```

The application will be available at <http://localhost:5173>

## API Endpoints

API documentation available at:

- <http://localhost:8000/docs> - Swagger UI
- <http://localhost:8000/redoc> - ReDoc

### GET /tasks

- Returns a list of all tasks
- Response: `200 OK`

```json
[
  {
    "id": 1,
    "description": "Example task",
    "created_at": "2024-01-20T10:00:00Z"
  }
]
```

### POST /tasks

- Creates a new task
- Request body:

```json
{
  "description": "New task"
}
```

- Response: `201 Created`

### DELETE /tasks/{id}

- Deletes a task by ID
- Response: `204 No Content`
- Returns `404 Not Found` if task doesn't exist

## Testing

### Frontend Tests

```bash
cd frontend
npm run test:unit
```

### Backend Tests

```bash
cd backend
poetry run pytest
```

## Common Issues

### Database Connection

- Ensure PostgreSQL is running
- Verify database exists: `psql -l | grep task_management`
- Check connection URL matches your PostgreSQL setup
- Default credentials are username: 'postgres', password: 'postgres'

### Port Conflicts

- Backend default port: 8000
- Frontend default port: 5173
- If ports are in use, you can modify:
  - Backend: Use `uvicorn app.main:app --reload --port <port>`
  - Frontend: Update `vite.config.ts`
