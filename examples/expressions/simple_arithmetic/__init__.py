"""Simple arithmetic expression in a template."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Main entry point."""
    name = "viewdom"
    result = render(html("<div>Hello {1 + 3}</div>"))
    return result
