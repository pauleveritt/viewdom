"""
Simplest example of rendering a static vdom, no variables.
"""

from viewdom import html, render

result = render(html('<div>Hello World</div>'))
expected = '<div>Hello World</div>'


def test():
    return expected, result
