<template>
  <div class="task-list">
    <div
      v-if="tasks.length === 0"
      data-test="empty-state"
      class="text-center py-4 text-gray-500"
    >
      No tasks available
    </div>

    <ul v-else class="space-y-2">
      <li
        v-for="task in tasks"
        :key="task.id"
        data-test="task-item"
        class="flex items-center justify-between p-4 bg-white rounded shadow"
      >
        <span>{{ task.description }}</span>
        <button
          @click="$emit('delete-task', task.id)"
          data-test="delete-button"
          class="px-3 py-1 text-red-600 hover:bg-red-50 rounded"
        >
          Delete
        </button>
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
