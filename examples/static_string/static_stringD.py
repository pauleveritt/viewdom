"""
Child nodes become part of the VDOM.
"""
from viewdom import html
from viewdom import render

vdom = html("<div>Hello <span>World<em>!</em></span></div>")
result = render(vdom)
expected = "<div>Hello <span>World<em>!</em></span></div>"


def test():
    return expected, result
