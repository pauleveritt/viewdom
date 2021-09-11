"""Show the component in the VDOM."""
from viewdom import VDOMNode
from viewdom import html


def Heading():
    return html("<h1>My Title</h1>")


def main() -> VDOMNode:
    vdom = html("<{Heading} />")
    return vdom
