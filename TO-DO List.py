# Define a class for tasks
class Task:
    def _init_(self, description, completed=False):
        self.description = description
        self.completed = completed

    def _str_(self):
        status = "X" if self.completed else " "
        return f"[{status}] {self.description}"

# Define a class for the to-do list
class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def _str_(self):
        return "\n".join(f"{i+1}. {task}" for i, task in enumerate(self.tasks))

# Example usage:
todo_list = ToDoList()
todo_list.add_task("Buy groceries")
todo_list.add_task("Finish homework")
todo_list.add_task("Call mom")
print("Initial to-do list:")
print(todo_list)

# Mark task as complete and delete a task
todo_list.mark_task_complete(1)
todo_list.delete_task(0)
print("\nUpdated to-do list:")
print(todo_list)