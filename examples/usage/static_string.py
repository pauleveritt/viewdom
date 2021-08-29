"""
Render a static string, no markup.
"""

from viewdom import html, render

result = render(html('<div>Hello World</div>'))
expected = '<div>Hello World</div>'


def test():
    return expected, result
