"""Test an example."""
from viewdom import VDOMNode
from . import main
from . import Heading


def test_main() -> None:
    """Ensure the demo matches expected."""
    assert main() == VDOMNode(tag=Heading, props={}, children=[])
