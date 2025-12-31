"""Main entry point for the Todo App."""

from src.todo_app.todo_manager import TodoManager
from src.todo_app.cli import CLI


def main() -> None:
    """Run the main application loop."""
    print("Welcome to the Todo App!")
    print("Available commands: add, list, update, delete, complete, quit")
    
    todo_manager = TodoManager()
    cli = CLI(todo_manager)
    
    while True:
        try:
            command = input("\n> ").strip()
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