"""The base Heading is used in most cases except for a context."""
from hopscotch import Registry

from .app import Customer
from .app import Heading  # noqa: F401
from viewdom import html
from viewdom import render


def main() -> tuple[str, str]:
    """Main entry point."""
    # At startup
    registry = Registry()
    registry.scan()

    # First request, no customer, context=None
    request_registry0 = Registry(parent=registry, context=None)
    vdom = html("<{Heading} />")
    result0 = render(vdom, registry=request_registry0)

    # Second request, context=customer
    customer = Customer(first_name="Marie")
    request_registry1 = Registry(parent=registry, context=customer)
    vdom = html("<{Heading} />")
    result1 = render(vdom, registry=request_registry1)

    return result0, result1
