"""Overrides and additions in a local site."""
from dataclasses import dataclass

from hopscotch import injectable
from hopscotch.operators import context

from . import Customer
from .app import Heading
from viewdom import html
from viewdom import VDOM


@injectable(kind=Heading, context=Customer)
@dataclass
class SiteHeading:
    """A heading customized to the site."""

    customer: Customer = context()

    def __call__(self) -> VDOM:
        """Render the component."""
        first_name = self.customer.first_name
        return html("<h1>Hello {first_name}</h1>")
