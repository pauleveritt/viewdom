"""Generate a list of VDOMs then use in a render."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Main entry point."""
    message = "Hello"
    names = ["World", "Universe"]
    items = [html("<li>{label}</li>") for label in names]
    result = render(
        html(
            """
      <ul title="{message}">
        {items}
      </li>
    """
        )
    )
    return result
