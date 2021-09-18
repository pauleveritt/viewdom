"""Get a variable from an import."""
from viewdom import html
from viewdom import render

from .. import name


def Hello():
    assert name
    return render(html("<div>Hello {name}</div>"))


def main() -> str:
    result = Hello()
    return result
