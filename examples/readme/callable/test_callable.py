"""Test an example."""
from . import main


def test_main() -> None:
    """Ensure the greeting matches what is expected."""
    assert main() == "<div>Hello viewdom</div>"
