"""
Getting a doctype into the rendered output is a bit tricky.
"""

from markupsafe import Markup

from viewdom import html, render

doctype = Markup('<!DOCTYPE html>\n')
vdom = html('{doctype}<div>Hello World</div>')
# Markup('<!DOCTYPE html>\n'), VDOMNode(tag='div', props={}, children=['Hello World'])]

result = render(vdom)
expected = '<!DOCTYPE html>\n<div>Hello World</div>'


def test():
    return expected, result
