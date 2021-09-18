"""Pass a component as a prop value."""
from viewdom import html
from viewdom import render


def DefaultHeading():
    return html("<h1>Default Heading</h1>")


def Body(heading):
    return html("<body><{heading} /></body>")


def main() -> str:
    result = render(html("<{Body} heading={DefaultHeading} />"))
    return result
