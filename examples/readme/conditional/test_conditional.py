"""Test an example."""
from . import main


def test_readme_conditional() -> None:
    """Ensure the result matches what is expected."""
    assert main() == "<h1>Show?</h1>Say Howdy"
