"""Loop over a sequence and generate nodes."""
from viewdom import html
from viewdom import render


def main() -> str:
    """Render a template to a string."""
    message = "Hello"
    names = ["World", "Universe"]

    result = render(
        html(
            """
      <ul title="{message}">
        {[
            html('<li>{name}</li>')
            for name in names
         ] }
      </li>
    """
        )
    )
    return result
