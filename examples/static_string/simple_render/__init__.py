"""Render a static string, no markup."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Main entry point."""
    result = render(html("<div>Hello World</div>"))
    return result
