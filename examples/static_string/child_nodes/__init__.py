"""Child nodes become part of the VDOM."""
from viewdom import html
from viewdom import render


def main() -> str:
    vdom = html("<div>Hello <span>World<em>!</em></span></div>")
    result = render(vdom)
    return result
