"""
Prop values from scope variables.
"""

from viewdom import html, render


def Heading(title):
    return html('<h1>{title}</h1>')


this_title = 'My Title'
result = render(html('<{Heading} title={this_title} />'))
expected = '<h1>My Title</h1>'


def test():
    return expected, result
