"""Main entry point for the Todo App."""

from .todo_manager import TodoManager
from .cli import CLI


def main() -> None:
    """Run the main application loop."""
    print("Welcome to the Todo App!")
    print("Available commands: add, list, update, delete, complete, quit, exit, q")

    todo_manager = TodoManager()
    cli = CLI(todo_manager)

    while True:
        try:
            command = input("todo-app> ").strip()
            should_continue = cli.handle_command(command)
            if not should_continue:
                break
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()