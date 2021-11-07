"""Components registered in Hopscotch."""
from dataclasses import dataclass

from hopscotch import injectable

from viewdom import html, VDOM


@injectable()
@dataclass
class Heading:
    """The default heading."""

    def __call__(self) -> VDOM:
        """Render the component."""
        return html("<h1>My Title</h1>")
