"""
Get a variable from an import.
"""

from viewdom import html, render
from .variables import name


def main():
    return render(html('<div>Hello {name}</div>'))


result = main()
expected = '<div>Hello viewdom</div>'


def test():
    return expected, result
