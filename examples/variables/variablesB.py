"""
Get a variable from an import.
"""
from .variables import name
from viewdom import html
from viewdom import render


def main():
    return render(html("<div>Hello {name}</div>"))


result = main()
expected = "<div>Hello viewdom</div>"


def test():
    return expected, result
