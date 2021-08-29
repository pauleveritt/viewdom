"""
Shorthand syntax for attribute values means no need for double quotes.
"""

from viewdom import html, render

vdom = html('<div class={"Container1".lower()}>Hello World</div>')
result = render(vdom)
expected = '<div class="container1">Hello World</div>'


def test():
    return expected, result
