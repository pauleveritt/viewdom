"""Render just a string literal."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Main entry point."""
    vdom = html("Hello World")
    result = render(vdom)
    return result
