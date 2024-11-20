<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-8">Task Management</h1>
    <TaskList :tasks="tasks" @delete-task="handleDeleteTask" />
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import TaskList from "./components/TaskList.vue";
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

const handleDeleteTask = (id: number) => {
  tasks.value = tasks.value.filter((task) => task.id !== id);
};
</script>
