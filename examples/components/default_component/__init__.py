"""Overriding a default "built-in" component."""
from viewdom import html
from viewdom import render


def DefaultHeading():  # pragma: nocover
    return html("<h1>Default Heading</h1>")


def OtherHeading():
    return html("<h1>Other Heading</h1>")


def Body(heading=DefaultHeading):
    return html("<body><{heading} /></body>")


def main() -> str:
    result = render(html("<{Body} heading={OtherHeading}/>"))
    return result
