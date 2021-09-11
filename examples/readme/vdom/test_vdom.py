"""Test an example."""
from viewdom import VDOMNode
from . import main


def test_readme_() -> None:
    """Ensure the demo matches expected."""
    expected = VDOMNode(tag="div", props={}, children=["Hello World"])
    assert main() == expected
