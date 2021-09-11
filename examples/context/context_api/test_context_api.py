"""Test an example."""
from . import main


def test_main() -> None:
    """Ensure the demo matches expected."""
    assert main() == "<nav><h1>My Site</h1></nav><h2>My Page</h2>"
