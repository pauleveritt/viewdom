"""Use Python expressions inside the curly brackets, like f-strings do."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Render a template to a string."""
    name = "viewdom"
    result = render(html("<div>Hello {name.upper()}</div>"))
    return result
