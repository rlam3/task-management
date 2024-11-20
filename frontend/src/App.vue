<template>
  <div
    class="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 flex items-center justify-center p-6"
  >
    <div class="w-full max-w-lg">
      <h1 class="text-4xl font-bold text-center mb-2 text-gray-800">
        Task Management
      </h1>
      <p class="text-center mb-8 text-gray-600">Keep track of your tasks</p>
      <div
        class="bg-white rounded-xl shadow-lg ring-1 ring-black ring-opacity-5 p-6"
      >
        <AddTask @add-task="handleAddTask" />
        <TaskList :tasks="tasks" @delete-task="handleDeleteTask" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import TaskList from "./components/TaskList.vue";
import AddTask from "./components/AddTask.vue";
import type { Task } from "./types/task";

const tasks = ref<Task[]>([
  {
    id: 1,
    description: "Complete TDD implementation",
    created_at: new Date().toISOString(),
  },
  {
    id: 2,
    description: "Write more tests",
    created_at: new Date().toISOString(),
  },
]);

const handleAddTask = (description: string) => {
  const newTask: Task = {
    id: tasks.value.length + 1,
    description,
    created_at: new Date().toISOString(),
  };
  tasks.value = [newTask, ...tasks.value];
};

const handleDeleteTask = (id: number) => {
  tasks.value = tasks.value.filter((task) => task.id !== id);
};
</script>
