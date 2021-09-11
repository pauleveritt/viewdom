"""
Render just a string literal.
"""
from viewdom import html
from viewdom import render

vdom = html("Hello World")
result = render(vdom)
expected = "Hello World"


def test():
    return expected, result
