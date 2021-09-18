"""Subcomponents."""
from viewdom import html
from viewdom import render

title = "My Todos"


def Todo(label):
    return html("<li>{label}</li>")


def TodoList(todos):
    return html("<ul>{[Todo(label) for label in todos]}</ul>")


def main() -> str:
    todos = ["first"]
    return render(
        html(
            """
      <h1>{title}</h1>
      <{TodoList} todos={todos} />
    """
        )
    )
