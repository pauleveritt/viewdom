"""
Use "props" as attributes on a template node.
"""

from viewdom import html, render

name = 'viewdom'
this_id = 42

result = render(
    html('<div id={f"id-{this_id}"} title="{name}">Hello {name}</div>')
)
expected = '<div id="id-42" title="viewdom">Hello viewdom</div>'


def test():
    return expected, result
