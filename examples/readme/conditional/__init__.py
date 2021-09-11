"""Only show some templating blocks in certain conditions."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Render some markup."""
    message = "Say Howdy"
    not_message = "So Sad"
    show_message = True
    result = render(
        html(
            """
        <h1>Show?</h1>
        {message if show_message else not_message}
    """
        )
    )
    return result
