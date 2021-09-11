"""
Use a simple Python expression as the attribute value.
"""
from viewdom import html
from viewdom import render

vdom = html('<div class="container{1}">Hello World</div>')
result = render(vdom)
expected = '<div class="container1">Hello World</div>'


def test():
    return expected, result
