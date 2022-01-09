"""Loop through values in a template and render them."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Main entry point."""
    message = "Hello"
    names = ["World", "Universe"]
    result = render(
        html(
            """
            <ul title="{message}">
                {[
                    html('<li>{name}</li>')
                    for name in names
                ]}
            </ul>
            """
        )
    )
    return result
