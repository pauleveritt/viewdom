"""Get a variable from an import."""
from .. import name  # noqa F401
from viewdom import html
from viewdom import render


def Hello():
    """A simple hello component."""
    return render(html("<div>Hello {name}</div>"))


def main() -> str:
    """Main entry point."""
    result = Hello()
    return result
