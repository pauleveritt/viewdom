"""An expression which chooses subcomponent based on condition."""
from viewdom import html
from viewdom import render


def DefaultHeading():
    """The default heading."""
    return html("<h1>Default Heading</h1>")


def OtherHeading():
    """Another heading used in another condition."""
    return html("<h1>Other Heading</h1>")


def Body(heading=None):
    """Render the body with a heading based on which is passed in."""
    return html("<body>{heading if heading else DefaultHeading}</body>")


def main() -> str:
    """Main entry point."""
    result = render(html("<{Body} heading={OtherHeading}/>"))
    return result
