"""
Pass a component as a prop value.
"""

from viewdom import html, render


def DefaultHeading():
    return html('<h1>Default Heading</h1>')


def OtherHeading():  # pragma: nocover
    return html('<h1>Other Heading</h1>')


def Body(heading):
    return html('<body><{heading} /></body>')


result = render(html('<{Body} heading={DefaultHeading} />'))
expected = '<body><h1>Default Heading</h1></body>'


def test():
    return expected, result
