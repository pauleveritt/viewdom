"""Optional props."""
from viewdom import html
from viewdom import render


def Heading(title="My Title"):
    """The default heading."""
    return html("<h1>{title}</h1>")


def main() -> str:
    """Main entry point."""
    result = render(html("<{Heading} />"))
    return result
