"""Pass a simple prop to a component."""
from viewdom import html
from viewdom import render


def Heading(children):
    return html("<h1>My Title</h1><div>{children}</div>")


def main() -> str:
    result = render(html("<{Heading}>Hi<//>"))
    return result
