"""Simple example of inserting a variable value into a template."""
from viewdom import html
from viewdom import render


def main() -> str:
    name = "viewdom"
    result = render(html("<div>Hello {name}</div>"))
    return result
