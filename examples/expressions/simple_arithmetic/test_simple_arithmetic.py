"""Test an example."""
from . import main


def test_main() -> None:
    """Ensure the demo matches expected."""
    assert main() == "<div>Hello 4</div>"
