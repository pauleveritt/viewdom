"""
Markup gets escaped when inserted.
"""

from viewdom import html, render

body = '<span>Escaping</span>'
result = render(html('<div>{body}</div>'))
expected = '<div>&lt;span&gt;Escaping&lt;/span&gt;</div>'


def test():
    return expected, result
