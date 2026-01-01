"""Task model for the Todo App."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """Represents a single task in the todo list."""

    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

    def __post_init__(self):
        """Validate task attributes after initialization."""
        if len(self.title) > 255:
            raise ValueError("Task title cannot exceed 255 characters")
        if self.description and len(self.description) > 1000:
            raise ValueError("Task description cannot exceed 1000 characters")