"""
Use Python expressions inside the curly brackets, like f-strings do.
"""

from viewdom import html, render

name = 'viewdom'

result = render(html('<div>Hello {name.upper()}</div>'))
expected = '<div>Hello VIEWDOM</div>'


def test():
    return expected, result
