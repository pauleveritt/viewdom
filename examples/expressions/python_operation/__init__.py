"""Python operation in the expression."""
from viewdom import html
from viewdom import render



def main() -> str:
    name = "viewdom"
    result = render(html("<div>Hello {name.upper()}</div>"))
    return result
