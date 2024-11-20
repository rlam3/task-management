import { describe, it, expect } from "vitest";
import { mount } from "@vue/test-utils";
import TaskList from "../TaskList.vue";
import type { Task } from "../../types/task";

describe("TaskList", () => {
  it("displays empty state when there are no tasks", () => {
    const wrapper = mount(TaskList, {
      props: {
        tasks: []
      }
    });

    expect(wrapper.find('[data-test="empty-state"]').exists()).toBe(true);
    expect(wrapper.text()).toContain("No tasks available");
  });

  it("renders a list of tasks when tasks exist", () => {
    const tasks: Task[] = [
      {
        id: 1,
        description: "Complete TDD implementation",
        created_at: "2024-01-20T10:00:00Z"
      },
      {
        id: 2,
        description: "Write more tests",
        created_at: "2024-01-20T11:00:00Z"
      }
    ];

    const wrapper = mount(TaskList, {
      props: {
        tasks
      }
    });

    const taskItems = wrapper.findAll('[data-test="task-item"]');
    expect(taskItems).toHaveLength(2);
    expect(taskItems[0].text()).toContain("Complete TDD implementation");
    expect(taskItems[1].text()).toContain("Write more tests");
  });

  it("emits delete-task event when delete button is clicked", async () => {
    const tasks: Task[] = [{
      id: 1,
      description: "Task to delete",
      created_at: "2024-01-20T10:00:00Z"
    }];

    const wrapper = mount(TaskList, {
      props: {
        tasks
      }
    });

    await wrapper.find('[data-test="delete-button"]').trigger("click");

    expect(wrapper.emitted("delete-task")).toBeTruthy();
    expect(wrapper.emitted("delete-task")?.[0]).toEqual([1]); // Emitted with task id
  });
});
