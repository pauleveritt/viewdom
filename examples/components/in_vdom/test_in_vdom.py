"""Test an example."""
from . import Heading
from . import main
from viewdom import VDOMNode


def test_main() -> None:
    """Ensure the demo matches expected."""
    assert main() == VDOMNode(tag=Heading, props={}, children=[])
