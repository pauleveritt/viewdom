"""Test an example."""
from . import main


def test_readme_props() -> None:
    """Ensure the demo matches expected."""
    assert main() == '<div id="id-42" title="viewdom">Hello viewdom</div>'
