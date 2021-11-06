"""Get a variable from a passed-in ``prop``."""
from viewdom import html
from viewdom import render


def Hello(name):
    """A simple hello component."""
    return render(html("<div>Hello {name}</div>"))


def main() -> str:
    """Main entry point."""
    result = Hello(name="viewdom")
    return result
