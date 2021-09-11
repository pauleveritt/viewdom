"""Inserting a variable from the scope."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Render a template to a string."""
    name = "viewdom"
    result = render(html("<div>Hello {name}</div>"))
    return result
