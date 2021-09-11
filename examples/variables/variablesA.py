"""
Insert a variable from the local scope.
"""
from viewdom import html
from viewdom import render


def main():
    name = "viewdom"
    return render(html("<div>Hello {name}</div>"))


result = main()
expected = "<div>Hello viewdom</div>"


def test():
    return expected, result
