import pytest

from .examples import e01, e01a, e02, e03, e04, e05, e06


@pytest.mark.parametrize(
    'target',
    [
        e01,
        e01a,
        e02,
        e03,
        e04,
        e05,
        e06,
    ]
)
def test_docs_index(target):
    assert target.expected == target.result
