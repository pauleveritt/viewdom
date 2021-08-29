"""
Optional props.
"""

from viewdom import html, render


def Heading(title='My Title'):
    return html('<h1>{title}</h1>')


result = render(html('<{Heading} />'))
expected = '<h1>My Title</h1>'


def test():
    return expected, result
