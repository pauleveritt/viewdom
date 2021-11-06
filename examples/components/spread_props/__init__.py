"""Mimic ES6 spread operator to de-structure props."""
from viewdom import html
from viewdom import render


def Heading(title, this_id):
    """The default heading."""
    return html("<div title={title} id={this_id}>Hello</div>")


def main() -> str:
    """Main entry point."""
    props = dict(title="My Title", this_id="d1")
    result = render(html("<{Heading} ...{props}>Child<//>"))
    return result
