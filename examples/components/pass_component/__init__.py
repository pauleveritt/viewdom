"""Pass a component as a prop value."""
from viewdom import html
from viewdom import render


def DefaultHeading():
    """The default heading."""
    return html("<h1>Default Heading</h1>")


def Body(heading):
    """The body which renders the heading."""
    return html("<body><{heading} /></body>")


def main() -> str:
    """Main entry point."""
    result = render(html("<{Body} heading={DefaultHeading} />"))
    return result
