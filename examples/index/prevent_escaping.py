"""
Markup can be inserted when wrapped with a helper.
"""

from markupsafe import Markup

from viewdom import html, render

body = Markup('<span>No Escaping</span>')
result = render(html('<div>{body}</div>'))
expected = '<div><span>No Escaping</span></div>'


def test():
    return expected, result
