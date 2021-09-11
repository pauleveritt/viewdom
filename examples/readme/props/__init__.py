"""Use "props" as attributes on a template node."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Render a template to a string."""
    name = "viewdom"
    this_id = 42

    result = render(html('<div id={f"id-{this_id}"} title="{name}">Hello {name}</div>'))
    return result
