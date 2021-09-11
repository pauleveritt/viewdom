"""An expression which chooses subcomponent based on condition."""
from viewdom import html
from viewdom import render


def DefaultHeading():  # pragma: nocover
    return html("<h1>Default Heading</h1>")


def OtherHeading():
    return html("<h1>Other Heading</h1>")


def Body(heading=None):
    return html("<body>{heading if heading else DefaultHeading}</body>")


def main() -> str:
    result = render(html("<{Body} heading={OtherHeading}/>"))
    return result
