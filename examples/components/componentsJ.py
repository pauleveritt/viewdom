"""A variation of the to do list, possibly duplicated in another example."""
from dataclasses import dataclass
from typing import Iterable

from viewdom import html
from viewdom import render
from viewdom import VDOM


def Todo(label):
    """An individual to do component."""
    return html("<li>{label}</li>")


@dataclass
class TodoList:
    """A class-based to do list with passed-in data."""

    todos: Iterable

    def __call__(self) -> VDOM:
        """Render to a string."""
        return html("<ul>{[Todo(label) for label in self.todos]}</ul>")


def TodoApp(title, todolist):
    """A to do list application."""
    return html("<h1>{title}</h1>{todolist}")


def main():
    """Main entry point."""
    todos = ["first"]
    tl = TodoList(todos)
    return render(
        html(
            """
      <{TodoApp} title="My Todos" todolist={tl} />
    """
        )
    )


result = main()
expected = "<h1>My Todos</h1><ul><li>first</li></ul>"


def main() -> str:
    """Main entry point."""
    return result
