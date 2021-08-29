"""
Show the component in the VDOM.
"""

from viewdom import html, VDOMNode


def Heading():
    return html('<h1>My Title</h1>')  # pragma: nocover


vdom = html('<{Heading} />')
expected = VDOMNode(tag=Heading, props={}, children=[])  # type: ignore


def test():
    return expected, vdom
