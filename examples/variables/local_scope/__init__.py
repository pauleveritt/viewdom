"""Insert a variable from the local scope."""
from viewdom import html
from viewdom import render


def Hello():
    name = "viewdom"
    return render(html("<div>Hello {name}</div>"))


def main() -> str:
    result = Hello()
    return result
