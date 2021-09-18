"""Call a function from inside a template expression."""
from viewdom import html
from viewdom import render


def make_bigly(name: str) -> str:
    return f"BIGLY: {name.upper()}"


def main() -> str:
    name = "viewdom"
    result = render(html("<div>Hello {make_bigly(name)}</div>"))
    return result
