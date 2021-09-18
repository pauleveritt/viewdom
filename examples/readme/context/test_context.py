"""Test an example."""
from . import main


def test_readme_context() -> None:
    """Ensure the demo matches the expected."""
    assert main() == "<h1>My Todos</h1><ul><li>Item: first</li></ul>"
