"""The prop has a default value, so caller doesn't have to provide it."""
from viewdom import html
from viewdom import render


def Hello(name="viewdom"):
    return render(html("<div>Hello {name}</div>"))


def main() -> str:
    result = Hello()
    return result
