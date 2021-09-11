"""Split generating and rendering into two steps."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Render a template to a string."""
    vdom = html("<div>Hello World</div>")
    result = render(vdom)
    return result
