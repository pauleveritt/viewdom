"""Simple function component, nothing dynamic, that returns a VDOM."""
from viewdom import html
from viewdom import render


def Heading():
    """The default heading."""
    return html("<h1>My Title</h1>")


def main() -> str:
    """Main entry point."""
    vdom = html("<{Heading} />")
    result = render(vdom)
    return result
