"""
Show the VDOM itself.
"""
from viewdom import html
from viewdom import VDOMNode

result = html('<div class="container">Hello World</div>')
expected = VDOMNode(tag="div", props={"class": "container"}, children=["Hello World"])


def test():
    return expected, result
