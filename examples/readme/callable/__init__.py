"""Components can be any kind of callable."""
from dataclasses import dataclass

from viewdom import html
from viewdom import render


@dataclass
class Greeting:
    """Give a greeting."""

    name: str

    def __call__(self):
        """Render to a string."""
        return f"Hello {self.name}"


def main() -> str:
    """Render a template to a string."""
    greeting = Greeting(name="viewdom")
    result = render(html("<div><{greeting} /></div>"))
    return result
