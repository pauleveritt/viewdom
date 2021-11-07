"""Child nodes become part of the VDOM."""
from viewdom import html
from viewdom import VDOMNode


def main() -> VDOMNode:
    """Main entry point."""
    vdom = html("<div>Hello <span>World<em>!</em></span></div>")
    return vdom
