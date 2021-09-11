"""Pass a Python symbol as part of an expression."""
from viewdom import html
from viewdom import render


def Heading(title):
    return html("<h1>{title}</h1>")


def main() -> str:
    result = render(html('<{Heading} title={"My Title"} />'))
    return result
