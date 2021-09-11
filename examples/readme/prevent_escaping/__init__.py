"""Markup can be inserted when wrapped with a helper."""
from markupsafe import Markup

from viewdom import html
from viewdom import render


def main() -> str:
    """Render a template to a string."""
    body = Markup("<span>No Escaping</span>")
    result = render(html("<div>{body}</div>"))
    return result
