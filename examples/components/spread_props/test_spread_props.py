"""Test an example."""
from . import main


def test_main() -> None:
    """Ensure the demo matches expected."""
    assert main() == '<div title="My Title" id="d1">Hello</div>'
