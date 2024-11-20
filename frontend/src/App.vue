<template>
  <div class="min-h-screen bg-gray-100 flex items-center justify-center p-6">
    <div class="w-full max-w-lg">
      <h1 class="text-4xl font-bold text-center mb-2 text-gray-800">
        Task Management
      </h1>
      <p class="text-center mb-8 text-gray-600">Keep track of your tasks</p>
      <div
        class="bg-white rounded-xl shadow-lg ring-1 ring-black ring-opacity-5"
      >
        <div v-if="error" class="p-4 bg-red-50 text-red-600 rounded-t-xl">
          {{ error }}
        </div>
        <AddTask @add-task="handleAddTask" :loading="loading" />
        <TaskList :tasks="tasks" @delete-task="handleDeleteTask" />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import TaskList from "./components/TaskList.vue";
import AddTask from "./components/AddTask.vue";
import type { Task } from "./types/task";
import { getTasks, createTask } from "./api/tasks";

const tasks = ref<Task[]>([]);
const loading = ref(false);
const error = ref<string | null>(null);

async function loadTasks() {
  try {
    loading.value = true;
    error.value = null;
    tasks.value = await getTasks();
  } catch (e) {
    error.value = "Failed to load tasks";
    console.error(e);
  } finally {
    loading.value = false;
  }
}

async function handleAddTask(description: string) {
  try {
    loading.value = true;
    error.value = null;
    const newTask = await createTask(description);
    tasks.value = [newTask, ...tasks.value];
  } catch (e) {
    error.value = "Failed to create task";
    console.error(e);
  } finally {
    loading.value = false;
  }
}

const handleDeleteTask = (id: number) => {
  tasks.value = tasks.value.filter((task) => task.id !== id);
};

onMounted(() => {
  loadTasks();
});
</script>
