"""Simple function component, nothing dynamic, that returns a VDOM."""
from viewdom import html
from viewdom import render
from hopscotch import Registry


def main() -> str:
    """Main entry point."""
    registry = Registry()
    registry.scan()
    vdom = html("<{Heading} />", registry=registry)
    result = render(vdom)
    return result
