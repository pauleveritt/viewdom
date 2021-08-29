"""
Generators as components.
"""

from viewdom import html, render


def Todos():
    for todo in ["First", "Second"]:
        yield html('<li>{todo}</li>')


result = render(html('<ul><{Todos}/></ul>'))
expected = '<ul><li>First</li><li>Second</li></ul>'


def test():
    return expected, result
