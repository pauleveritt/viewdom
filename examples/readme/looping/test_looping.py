"""Test an example."""
from . import main


def test_readme_looping() -> None:
    """Ensure the demo matches expected."""
    assert main() == '<ul title="Hello"><li>World</li><li>Universe</li></ul>'
