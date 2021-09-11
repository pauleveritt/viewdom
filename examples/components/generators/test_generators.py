"""Test an example."""
from . import main


def test_main() -> None:
    """Ensure the demo matches expected."""
    assert main() == "<ul><li>First</li><li>Second</li></ul>"
