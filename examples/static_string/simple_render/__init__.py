"""Render a static string, no markup."""
from viewdom import html
from viewdom import render


def main() -> str:
    result = render(html("<div>Hello World</div>"))
    return result
