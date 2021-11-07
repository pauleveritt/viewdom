"""Components registered in Hopscotch."""
from dataclasses import dataclass

from hopscotch import injectable

from viewdom import html
from viewdom import VDOM


# The class used as the "context"
@dataclass
class Customer:
    """The person to greet, stored as the registry context."""

    first_name: str


@injectable()
@dataclass
class Heading:
    """The default heading."""

    def __call__(self) -> VDOM:
        """Render the component."""
        return html("<h1>My Title</h1>")
