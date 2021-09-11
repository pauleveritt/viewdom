"""Test an example."""
from . import main


def test_readme_escaping() -> None:
    """Ensure the demo matches expected."""
    assert main() == "<div>&lt;span&gt;Escaping&lt;/span&gt;</div>"
