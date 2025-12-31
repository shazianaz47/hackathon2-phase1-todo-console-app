"""Todo Manager for the Todo App."""

from typing import List, Optional
from src.todo_app.task import Task


class TodoManager:
    """Manages the collection of tasks."""
    
    def __init__(self) -> None:
        """Initialize the todo manager with an empty list of tasks."""
        self._tasks: List[Task] = []
        self._next_id: int = 1
    
    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task with the given title and description."""
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description,
            completed=False
        )
        self._tasks.append(task)
        self._next_id += 1
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """Get all tasks."""
        return self._tasks.copy()
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID."""
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """Update a task's title and/or description."""
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()
        
        if description is not None:
            task.description = description
        
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID."""
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        self._tasks.remove(task)
        return True
    
    def toggle_task_completion(self, task_id: int) -> bool:
        """Toggle the completion status of a task."""
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        task.completed = not task.completed
        return True