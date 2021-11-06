"""Show the VDOM itself."""
from viewdom import html


def main() -> str:
    """Main entry point."""
    result = html('<div class="container">Hello World</div>')
    return result
