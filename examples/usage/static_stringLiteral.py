"""
Render just a string literal.
"""

from viewdom import html, render

vdom = html('Hello World')
result = render(vdom)
expected = 'Hello World'


def test():
    return expected, result
