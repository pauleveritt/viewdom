"""Children as props."""
from viewdom import html
from viewdom import render


def Heading(children, title):
    """The default heading."""
    return html("<h1>{title}</h1><div>{children}</div>")


def main() -> str:
    """Main entry point."""
    result = render(html('<{Heading} title="My Title">Child<//>'))
    return result
