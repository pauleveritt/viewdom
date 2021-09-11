"""Markup gets escaped when inserted."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Render a template to a string."""
    body = "<span>Escaping</span>"
    result = render(html("<div>{body}</div>"))
    return result
