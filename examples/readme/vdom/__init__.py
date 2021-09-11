"""Simplest example of generating a static vdom, no variables."""
from viewdom import VDOMNode
from viewdom import html


def main() -> VDOMNode:
    """Render a template to a string."""
    vdom = html("<div>Hello World</div>")
    return vdom
