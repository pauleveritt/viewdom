"""Render just a string literal."""
from viewdom import html
from viewdom import render


def main() -> str:
    vdom = html("Hello World")
    result = render(vdom)
    return result
