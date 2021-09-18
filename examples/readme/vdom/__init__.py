"""Simplest example of generating a static vdom, no variables."""
from viewdom import html
from viewdom import VDOMNode


def main() -> VDOMNode:
    """Render a template to a string."""
    vdom = html("<div>Hello World</div>")
    return vdom
