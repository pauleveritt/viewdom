"""
Python operation in the expression.
"""
from viewdom import html
from viewdom import render

name = "viewdom"
result = render(html("<div>Hello {name.upper()}</div>"))
expected = "<div>Hello VIEWDOM</div>"


def test():
    return expected, result
