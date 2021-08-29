"""
Pass a simple prop to a component.
"""

from viewdom import html, render


def Heading(children):
    return html('<h1>My Title</h1><div>{children}</div>')


result = render(html('<{Heading}>Hi<//>'))
expected = '<h1>My Title</h1><div>Hi</div>'


def test():
    return expected, result
