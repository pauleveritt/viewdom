"""
Get a variable from a passed-in ``prop``.
"""

from viewdom import html, render


def main(name):
    return render(html('<div>Hello {name}</div>'))


result = main(name='viewdom')
expected = '<div>Hello viewdom</div>'


def test():
    return expected, result
