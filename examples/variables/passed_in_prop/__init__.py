"""Get a variable from a passed-in ``prop``."""
from viewdom import html
from viewdom import render


def Hello(name):
    return render(html("<div>Hello {name}</div>"))


def main() -> str:
    result = Hello(name="viewdom")
    return result
