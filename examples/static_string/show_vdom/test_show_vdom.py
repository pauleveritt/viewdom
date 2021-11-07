"""Test an example."""
from . import main
from viewdom import VDOMNode


def test_main() -> None:
    """Ensure the demo matches expected."""
    assert main() == VDOMNode(
        tag="div", props={"class": "container"}, children=["Hello World"]
    )
