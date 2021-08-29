"""
Mimic ES6 spread operator to destructure props.
"""

from viewdom import html, render


def Heading(title, this_id):
    return html('<div title={title} id={this_id}>Hello</div>')


props = dict(title='My Title', this_id="d1")
result = render(html('<{Heading} ...{props}>Child<//>'))
expected = '<div title="My Title" id="d1">Hello</div>'


def test():
    return expected, result
