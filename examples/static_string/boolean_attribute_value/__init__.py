"""Boolean attribute values are reduced during rendering."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Main entry point."""
    vdom = html("<div editable={True}>Hello World</div>")
    result = render(vdom)
    return result
