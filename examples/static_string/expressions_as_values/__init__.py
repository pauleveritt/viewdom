"""Use a simple Python expression as the attribute value."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Main entry point."""
    vdom = html('<div class="container{1}">Hello World</div>')
    result = render(vdom)
    return result
