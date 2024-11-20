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

### Backend

1. Create PostgreSQL database:

```bash
createdb task_management
```

2. Install dependencies and run server:

```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload
```

The API will be available at <http://localhost:8000>

### Frontend

1. Install dependencies and run development server:

```bash
cd frontend
npm install
npm run dev
```

The application will be available at <http://localhost:5173>

## Project Structure

### Frontend

- `src/components/` - Vue components
- `src/api/` - API client
- `src/types/` - TypeScript types
- `src/components/__tests__/` - Component tests

### Backend

- `app/main.py` - FastAPI application and routes
- `app/models.py` - SQLAlchemy models
- `app/repositories.py` - Data access layer
- `app/database.py` - Database configuration
- `tests/` - Backend tests

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

## Current Status

✅ Project is complete with:

- [x] Frontend implementation
  - [x] Task list component
  - [x] Add task form
  - [x] API integration
  - [x] Error handling
  - [x] Loading states
  - [x] Unit tests

- [x] Backend implementation
  - [x] FastAPI setup
  - [x] Database integration
  - [x] Repository pattern
  - [x] CORS configuration
  - [x] Unit tests
