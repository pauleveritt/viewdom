"""Children as props."""
from viewdom import html
from viewdom import render


def Heading(children, title):
    return html("<h1>{title}</h1><div>{children}</div>")


def main() -> str:
    result = render(html('<{Heading} title="My Title">Child<//>'))
    return result
