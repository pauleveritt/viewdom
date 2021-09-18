"""Show the VDOM itself."""
from viewdom import html


def main() -> str:
    result = html('<div class="container">Hello World</div>')
    return result
