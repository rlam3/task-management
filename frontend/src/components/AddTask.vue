<template>
  <form @submit.prevent="handleSubmit" class="p-6 border-b border-gray-100">
    <div class="flex flex-col space-y-2">
      <input
        v-model="taskDescription"
        type="text"
        placeholder="Enter new task..."
        class="w-full px-4 py-2 border border-gray-200 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        :class="{ 'border-red-500': showError }"
        :disabled="loading"
      />
      <div
        v-if="showError"
        data-test="error-message"
        class="text-red-500 text-sm"
      >
        Task description is required
      </div>
      <button
        type="submit"
        class="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
        :disabled="loading"
      >
        {{ loading ? "Adding..." : "Add Task" }}
      </button>
    </div>
  </form>
</template>

<script setup lang="ts">
import { ref } from "vue";

defineProps<{
  loading?: boolean;
}>();

const emit = defineEmits<{
  (e: "add-task", description: string): void;
}>();

const taskDescription = ref("");
const showError = ref(false);

const handleSubmit = () => {
  if (!taskDescription.value.trim()) {
    showError.value = true;
    return;
  }

  showError.value = false;
  emit("add-task", taskDescription.value.trim());
  taskDescription.value = "";
};
</script>
