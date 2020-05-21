import pytest

from examples.index import e01, e01a, e02, e03, e04, e05, e06, e07


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
        e07
    ]
)
def test_docs_index(target):
    assert target.expected == target.result
