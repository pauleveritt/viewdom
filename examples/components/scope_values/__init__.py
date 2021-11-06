"""Prop values from scope variables."""
from viewdom import html
from viewdom import render


def Heading(title):
    """The default heading."""
    return html("<h1>{title}</h1>")


this_title = "My Title"


def main() -> str:
    """Main entry point."""
    result = render(html("<{Heading} title={this_title} />"))
    return result
