<template>
  <div class="p-6">
    <!-- Empty State -->
    <div
      v-if="tasks.length === 0"
      data-test="empty-state"
      class="text-center py-12"
    >
      <p class="text-gray-500 text-lg font-medium">No tasks available</p>
    </div>

    <!-- Task List -->
    <ul v-else class="divide-y divide-gray-100">
      <li
        v-for="task in tasks"
        :key="task.id"
        data-test="task-item"
        class="group py-4 flex flex-col items-center"
      >
        <span class="text-gray-800 text-lg font-medium mb-1">
          {{ task.description }}
        </span>
        <div class="flex items-center justify-between w-full">
          <span class="text-sm text-gray-500">
            {{
              new Date(task.created_at).toLocaleDateString("en-US", {
                weekday: "long",
                year: "numeric",
                month: "long",
                day: "numeric",
                hour: "2-digit",
                minute: "2-digit",
              })
            }}
          </span>
          <button
            @click="$emit('delete-task', task.id)"
            data-test="delete-button"
            class="px-3 py-1.5 text-sm text-red-600 font-medium rounded-md hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-opacity-50"
          >
            Delete
          </button>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import type { Task } from "../types/task";

defineProps<{
  tasks: Task[];
}>();

defineEmits<{
  (e: "delete-task", id: number): void;
}>();
</script>
