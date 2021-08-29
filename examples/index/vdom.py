"""
Simplest example of generating a static vdom, no variables.
"""

from viewdom import VDOMNode, html

# Make a VDOM
result = html('<div>Hello World</div>')

# Here's what the result will look like
expected = VDOMNode(tag='div', props={}, children=['Hello World'])


def test():
    return expected, result
