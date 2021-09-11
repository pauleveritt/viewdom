"""Simplest example of rendering a static vdom, no variables."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Render a template to a string."""
    result = render(html("<div>Hello World</div>"))
    return result
