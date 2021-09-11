"""Test an example."""
from . import main


def test_readme_expressions() -> None:
    """Ensure the demo matches expected."""
    assert main() == "<div>Hello VIEWDOM</div>"
