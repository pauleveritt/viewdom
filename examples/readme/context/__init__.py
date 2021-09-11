"""Avoid passing data down long trees as props by using a Context API."""
from viewdom import Context
from viewdom import html
from viewdom import render
from viewdom import use_context


def Todo(label):
    """Render a to do."""
    prefix = use_context("prefix")
    return html("<li>{prefix}{label}</li>")


def TodoList(these_todos):
    """Render a to do list."""
    return html("<ul>{[Todo(label) for label in these_todos]}</ul>")


def main() -> str:
    """Render a template to a string."""
    assert Context
    title = "My Todos"
    todos = ["first"]
    result = render(
        html(
            """
      <{Context} prefix="Item: ">
          <h1>{title}</h1>
          <{TodoList} these_todos={todos} />
      <//>
    """
        )
    )
    return result
