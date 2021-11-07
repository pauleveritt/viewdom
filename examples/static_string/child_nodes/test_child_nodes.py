"""Test an example."""
from . import main
from viewdom import VDOMNode


def test_main() -> None:
    """Ensure the demo matches expected."""
    assert main() == VDOMNode(
        tag="div",
        props={},
        children=[
            "Hello ",
            VDOMNode(
                tag="span",
                props={},
                children=["World", VDOMNode(tag="em", props={}, children=["!"])],
            ),
        ],
    )
