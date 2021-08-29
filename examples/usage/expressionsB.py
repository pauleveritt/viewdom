"""
Call a function from inside a template expression.
"""

from viewdom import html, render


def make_bigly(name: str) -> str:
    return f'BIGLY: {name.upper()}'


name = 'viewdom'
result = render(html('<div>Hello {make_bigly(name)}</div>'))
expected = '<div>Hello BIGLY: VIEWDOM</div>'


def test():
    return expected, result
