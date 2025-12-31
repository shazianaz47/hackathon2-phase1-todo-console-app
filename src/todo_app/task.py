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