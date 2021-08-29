"""
Use ``children`` as a built-in "prop".
"""

from viewdom import html, render


def Heading(title):
    return html('<h1>{title}</h1>')


result = render(html('<{Heading} title="My Title" />'))
expected = '<h1>My Title</h1>'


def test():
    return expected, result
