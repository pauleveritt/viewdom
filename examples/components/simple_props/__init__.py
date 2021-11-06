"""Use ``children`` as a built-in "prop"."""
from viewdom import html
from viewdom import render


def Heading(title):
    """Default heading."""
    return html("<h1>{title}</h1>")


def main() -> str:
    """Main entry point."""
    result = render(html('<{Heading} title="My Title" />'))
    return result
