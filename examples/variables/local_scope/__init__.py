"""Insert a variable from the local scope."""
from viewdom import html
from viewdom import render


def Hello():
    """A simple hello component."""
    name = "viewdom"
    return render(html("<div>Hello {name}</div>"))


def main() -> str:
    """Main entry point."""
    result = Hello()
    return result
