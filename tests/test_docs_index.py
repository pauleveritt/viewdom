import pytest

from examples.index import (
    render,
    split,
    scope,
    expressions,
    escaping,
    prevent_escaping,
    conditional,
    looping,
    components,
    context,
)


@pytest.mark.parametrize(
    'target',
    [
        render,
        split,
        scope,
        expressions,
        escaping,
        prevent_escaping,
        conditional,
        looping,
        components,
        context
    ]
)
def test_docs_index(target):
    assert target.expected == target.result
