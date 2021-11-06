"""Generators as components."""
from viewdom import html
from viewdom import render


def Todos():
    """A sequence of li items."""
    for todo in ["First", "Second"]:  # noqa B007
        yield html("<li>{todo}</li>")


def main() -> str:
    """Main entry point."""
    result = render(html("<ul><{Todos}/></ul>"))
    return result
