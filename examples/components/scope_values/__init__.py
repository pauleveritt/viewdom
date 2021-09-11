"""Prop values from scope variables."""
from viewdom import html
from viewdom import render


def Heading(title):
    return html("<h1>{title}</h1>")


this_title = "My Title"


def main() -> str:
    result = render(html("<{Heading} title={this_title} />"))
    return result
