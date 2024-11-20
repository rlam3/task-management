import type { Task } from '../types/task'

const API_URL = 'http://localhost:8000'

export async function getTasks(): Promise<Task[]> {
  const response = await fetch(`${API_URL}/tasks/`)
  if (!response.ok) {
    throw new Error('Failed to fetch tasks')
  }
  return response.json()
}

export async function createTask(description: string): Promise<Task> {
  const response = await fetch(`${API_URL}/tasks/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ description }),
  })
  if (!response.ok) {
    throw new Error('Failed to create task')
  }
  return response.json()
}

export async function deleteTask(id: number): Promise<void> {
  const response = await fetch(`${API_URL}/tasks/${id}`, {
    method: 'DELETE',
  })
  if (!response.ok) {
    throw new Error('Failed to delete task')
  }
}
