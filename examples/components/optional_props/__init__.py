"""Optional props."""
from viewdom import html
from viewdom import render


def Heading(title="My Title"):
    return html("<h1>{title}</h1>")


def main() -> str:
    result = render(html("<{Heading} />"))
    return result
