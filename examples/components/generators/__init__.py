"""Generators as components."""
from viewdom import html
from viewdom import render


def Todos():
    for todo in ["First", "Second"]:
        yield html("<li>{todo}</li>")


def main() -> str:
    result = render(html("<ul><{Todos}/></ul>"))
    return result
