"""Shorthand syntax for attribute values means no need for double quotes."""
from viewdom import html
from viewdom import render



def main() -> str:
    vdom = html('<div class={"Container1".lower()}>Hello World</div>')
    result = render(vdom)
    return result
