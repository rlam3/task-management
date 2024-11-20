# Task Management Application

A full-stack task management application built with FastAPI, PostgreSQL, and Vue.js.

## Development Approach

We're following a Test-Driven Development (TDD) approach:

1. Write failing tests
2. Write minimal code to pass tests
3. Refactor while keeping tests green

## Task List

### Frontend (Vue.js) - Phase 1

- [ ] Initial Setup
  - [ ] Create Vue.js project with Vite
  - [ ] Setup Tailwind CSS
  - [ ] Configure testing environment (Vitest)

- [ ] Task List Component
  - [ ] Write tests for TaskList component
  - [ ] Implement TaskList with mock data
  - [ ] Add empty state handling
  - [ ] Style with Tailwind CSS

- [ ] Add Task Component
  - [ ] Write tests for AddTask component
  - [ ] Implement form with validation
  - [ ] Add loading states
  - [ ] Style with Tailwind CSS

- [ ] Delete Task Feature
  - [ ] Write tests for delete functionality
  - [ ] Implement delete button
  - [ ] Add confirmation dialog
  - [ ] Handle loading/error states

### Backend (FastAPI) - Phase 2

- [ ] Initial Setup
  - [ ] Create FastAPI project structure
  - [ ] Setup PostgreSQL database
  - [ ] Configure testing environment (pytest)

- [ ] Task API
  - [ ] Write tests for GET /tasks endpoint
  - [ ] Write tests for POST /tasks endpoint
  - [ ] Write tests for DELETE /tasks/{id} endpoint
  - [ ] Implement endpoints with basic validation
  - [ ] Add error handling

- [ ] Database Integration
  - [ ] Create Task model
  - [ ] Setup database migrations
  - [ ] Implement database operations
  - [ ] Write integration tests

### Integration - Phase 3

- [ ] Frontend API Integration
  - [ ] Create API client service
  - [ ] Update components to use real API
  - [ ] Add error handling
  - [ ] Update tests with API mocking

- [ ] Final Testing
  - [ ] End-to-end testing
  - [ ] Cross-browser testing
  - [ ] Performance testing
  - [ ] Bug fixes

## Tech Stack

- Frontend:
  - Vue.js 3
  - Vite
  - Tailwind CSS
  - Vitest for unit testing

- Backend:
  - FastAPI
  - PostgreSQL
  - SQLAlchemy
  - pytest for testing

## Getting Started

Instructions for setting up the development environment will be added as we progress through the implementation.

## Current Status

🚧 Project is under active development 🚧
