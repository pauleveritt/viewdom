"""Test an example."""
from . import main


def test_readme_prevent_escaping() -> None:
    """Ensure the demo matches expected."""
    assert main() == "<div><span>No Escaping</span></div>"
