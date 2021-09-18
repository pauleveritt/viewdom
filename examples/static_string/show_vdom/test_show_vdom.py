"""Test an example."""
from viewdom import VDOMNode
from . import main


def test_main() -> None:
    """Ensure the demo matches expected."""
    assert main() == VDOMNode(
        tag="div", props={"class": "container"}, children=["Hello World"]
    )
