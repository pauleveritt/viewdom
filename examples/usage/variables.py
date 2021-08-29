"""
Simple example of inserting a variable value into a template.
"""

from viewdom import html, render

name = 'viewdom'
result = render(html('<div>Hello {name}</div>'))
expected = '<div>Hello viewdom</div>'


def test():
    return expected, result
