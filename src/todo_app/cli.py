"""Command Line Interface for the Todo App."""

from typing import Optional
from .todo_manager import TodoManager
from .task import Task


class CLI:
    """Handles command-line interface interactions."""

    def __init__(self, todo_manager: TodoManager) -> None:
        """Initialize the CLI with a todo manager."""
        self.todo_manager = todo_manager

    def display_tasks(self) -> None:
        """Display all tasks in a formatted list."""
        tasks = self.todo_manager.get_all_tasks()

        if not tasks:
            print("No tasks in the list.")
            return

        for task in tasks:
            status = "X" if task.completed else " "
            print(f"[{task.id}] [{status}] {task.title}")
            if task.description:
                print(f"      Description: {task.description}")

    def add_task(self) -> None:
        """Add a new task through CLI prompts."""
        title = input("Enter task title: ").strip()

        if not title:
            print("Error: Task title cannot be empty.")
            return

        # Validate title length
        if len(title) > 255:
            print("Error: Task title cannot exceed 255 characters.")
            return

        description = input("Enter task description (optional): ").strip()
        if not description:
            description = None

        # Validate description length
        if description and len(description) > 1000:
            print("Error: Task description cannot exceed 1000 characters.")
            return

        try:
            task = self.todo_manager.add_task(title, description)
            print(f"Task added with ID {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def update_task(self) -> None:
        """Update an existing task through CLI prompts."""
        task_id_input = input("Enter task ID to update: ").strip()
        if not task_id_input.isdigit():
            print("Error: Invalid task ID. Please enter a number.")
            return

        try:
            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return

        # Check if task exists
        task = self.todo_manager.get_task_by_id(task_id)
        if task is None:
            print(f"Error: Task with ID {task_id} does not exist.")
            return

        # Get new title
        new_title = input(f"Enter new title (current: '{task.title}'): ").strip()
        if not new_title:
            new_title = None  # Keep existing title
        elif len(new_title) > 255:
            print("Error: Task title cannot exceed 255 characters.")
            return

        # Get new description
        current_desc = task.description if task.description else ""
        new_description = input(f"Enter new description (current: '{current_desc}'): ").strip()
        if not new_description:
            new_description = None  # Keep existing description or set to None
        elif len(new_description) > 1000:
            print("Error: Task description cannot exceed 1000 characters.")
            return

        try:
            updated = self.todo_manager.update_task(task_id, new_title, new_description)
            if updated:
                print(f"Task {task_id} updated successfully.")
            else:
                print(f"Error: Failed to update task {task_id}.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_task(self) -> None:
        """Delete a task by ID through CLI prompt."""
        task_id_input = input("Enter task ID to delete: ").strip()
        if not task_id_input.isdigit():
            print("Error: Invalid task ID. Please enter a number.")
            return

        try:
            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return

        deleted = self.todo_manager.delete_task(task_id)
        if deleted:
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Error: Task with ID {task_id} does not exist.")

    def complete_task(self) -> None:
        """Toggle completion status of a task by ID through CLI prompt."""
        task_id_input = input("Enter task ID to mark as complete/incomplete: ").strip()
        if not task_id_input.isdigit():
            print("Error: Invalid task ID. Please enter a number.")
            return

        try:
            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return

        toggled = self.todo_manager.toggle_task_completion(task_id)
        if toggled:
            task = self.todo_manager.get_task_by_id(task_id)
            status = "completed" if task.completed else "incomplete"
            print(f"Task {task_id} marked as {status}.")
        else:
            print(f"Error: Task with ID {task_id} does not exist.")

    def handle_command(self, command: str) -> bool:
        """Handle a command from the user.

        Returns True if the application should continue, False to exit.
        """
        command_parts = command.strip().split()
        if not command_parts:
            return True  # Continue running

        cmd = command_parts[0].lower()

        if cmd in ["quit", "exit", "q"]:
            return False  # Exit the application

        if cmd == "list":
            self.display_tasks()
        elif cmd == "add":
            self.add_task()
        elif cmd == "update":
            self.update_task()
        elif cmd == "delete":
            self.delete_task()
        elif cmd in ["complete", "done"]:
            self.complete_task()
        else:
            print(f"Unknown command: {cmd}")
            print("Available commands: add, list, update, delete, complete, quit, exit, q")

        return True  # Continue running