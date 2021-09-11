"""Test an example."""
from . import main


def test_readme_components() -> None:
    """Ensure the greeting matches what is expected."""
    assert main() == "<h1>My Todos</h1><ul><li>first</li></ul>"
