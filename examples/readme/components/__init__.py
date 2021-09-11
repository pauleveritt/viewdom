"""Break a large template into smaller, re-usable component."""
from viewdom import html
from viewdom import render


def Todo(label):
    """Render a to do."""
    return html("<li>{label}</li>")


def TodoList(todos):
    """Render a list of to dos."""
    return html("<ul>{[Todo(label) for label in todos]}</ul>")


def main() -> str:
    """Render a template to a string."""
    title = "My Todos"
    todos = ["first"]

    result = render(
        html(
            """
      <h1>{title}</h1>
      <{TodoList} todos={todos} />
    """
        )
    )
    return result
