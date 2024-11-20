import { describe, it, expect } from "vitest";
import { mount } from "@vue/test-utils";
import AddTask from "../AddTask.vue";

describe("AddTask", () => {
  it("emits add-task event with task description when form is submitted", async () => {
    const wrapper = mount(AddTask);
    const input = wrapper.find('input[type="text"]');
    const form = wrapper.find("form");

    await input.setValue("New test task");
    await form.trigger("submit.prevent");

    expect(wrapper.emitted("add-task")).toBeTruthy();
    expect(wrapper.emitted("add-task")?.[0]).toEqual(["New test task"]);
    // Check if input was cleared
    const inputElement = input.element as HTMLInputElement;
    expect(inputElement.value).toBe("");
  });

  it("does not emit add-task event when input is empty", async () => {
    const wrapper = mount(AddTask);
    const form = wrapper.find("form");

    await form.trigger("submit.prevent");

    expect(wrapper.emitted("add-task")).toBeFalsy();
  });

  it("shows validation message when trying to submit empty input", async () => {
    const wrapper = mount(AddTask);
    const form = wrapper.find("form");

    await form.trigger("submit.prevent");

    expect(wrapper.find('[data-test="error-message"]').exists()).toBe(true);
    expect(wrapper.text()).toContain("Task description is required");
  });
});
