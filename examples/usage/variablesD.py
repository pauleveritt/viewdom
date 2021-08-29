"""
The prop has a default value, so caller doesn't have to provide it.
"""

from viewdom import html, render


def main(name='viewdom'):
    return render(html('<div>Hello {name}</div>'))


result = main()
expected = '<div>Hello viewdom</div>'


def test():
    return expected, result
