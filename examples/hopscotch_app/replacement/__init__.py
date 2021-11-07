"""Replace a built-in component using a local site registration."""
from hopscotch import Registry

from .app import Heading  # noqa: F401
from viewdom import html
from viewdom import render


def main() -> str:
    """Main entry point."""
    # At startup
    registry = Registry()
    registry.scan()

    # Per request
    vdom = html("<{Heading} />")
    result = render(vdom, registry=registry)
    return result
