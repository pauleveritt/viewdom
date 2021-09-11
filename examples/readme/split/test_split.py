"""Test an example."""
from . import main


def test_readme_() -> None:
    """Ensure the demo matches expected."""
    assert main() == "<div>Hello World</div>"
