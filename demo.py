#!/usr/bin/env python3
"""
Demo script for hackathon judges to showcase the Todo App functionality.
This script demonstrates all 5 core features of the application.
"""

import sys
from src.todo_app.todo_manager import TodoManager
from src.todo_app.cli import CLI


def run_demo():
    """Run the demo sequence for hackathon judges."""
    print("Todo App Demo for Hackathon Judges")
    print("=" * 35)

    # Initialize the application components
    todo_manager = TodoManager()
    cli = CLI(todo_manager)

    print("\n1. ADDING TASKS")
    print("-" * 15)
    print("Adding sample tasks...")

    # Add some sample tasks
    todo_manager.add_task("Buy groceries", "Milk, eggs, bread")
    todo_manager.add_task("Finish Python project", "Complete TODO app for hackathon")
    todo_manager.add_task("Call mom", "Wish her happy birthday")

    print("Added 3 tasks to the list")

    print("\n2. VIEWING ALL TASKS")
    print("-" * 19)
    print("Displaying all tasks...")
    cli.display_tasks()

    print("\n3. MARKING TASKS AS COMPLETE")
    print("-" * 25)
    print("Marking task #1 as complete...")

    # Manually toggle completion for demo purposes
    todo_manager.toggle_task_completion(1)
    print("Task #1 marked as complete!")

    print("\nViewing tasks after marking #1 as complete:")
    cli.display_tasks()

    print("\n4. UPDATING TASKS")
    print("-" * 15)
    print("Updating task #2...")

    # Update a task
    todo_manager.update_task(2, "Finish Python project - Phase 1", "Complete core features of TODO app")
    print("Task #2 updated!")

    print("\nViewing tasks after update:")
    cli.display_tasks()

    print("\n5. DELETING TASKS")
    print("-" * 15)
    print("Deleting task #3...")

    # Delete a task
    todo_manager.delete_task(3)
    print("Task #3 deleted!")

    print("\nFinal task list:")
    cli.display_tasks()

    print("\nDEMO COMPLETE!")
    print("All 5 core features demonstrated successfully:")
    print("  1. Add Task")
    print("  2. View Task List")
    print("  3. Mark as Complete")
    print("  4. Update Task")
    print("  5. Delete Task")

    print("\nThank you for your attention!")


if __name__ == "__main__":
    run_demo()