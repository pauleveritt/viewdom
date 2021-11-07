"""Overrides and additions in a local site."""
from dataclasses import dataclass

from hopscotch import injectable

from .app import Heading
from viewdom import html
from viewdom import VDOM


@injectable(kind=Heading)
@dataclass
class SiteHeading:
    """A heading customized to the site."""

    def __call__(self) -> VDOM:
        """Render the component."""
        return html("<h1>Local Site Title</h1>")
