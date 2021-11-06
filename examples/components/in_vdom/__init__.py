"""Show the component in the VDOM."""
from viewdom import html
from viewdom import VDOMNode


def Heading():
    """The default heading."""
    return html("<h1>My Title</h1>")


def main() -> VDOMNode:
    """Main entry point."""
    vdom = html("<{Heading} />")
    return vdom
