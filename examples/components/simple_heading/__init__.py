"""Simple function component that returns a VDOM."""
from viewdom import html
from viewdom import render


def Heading():
    return html("<h1>My Title</h1>")


def main() -> str:
    vdom = html("<{Heading} />")
    result = render(vdom)
    return result
