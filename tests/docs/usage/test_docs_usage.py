import pytest

from .examples import (
    static_string,
    static_stringA,
    static_stringB,
    static_stringC,
    static_stringD,
    variables,
    variablesA,
    expressions,
    expressionsA,
    conditional,
    looping,
    components,
    context,
)


@pytest.mark.parametrize(
    'target',
    [
        static_string,
        static_stringA,
        static_stringB,
        static_stringC,
        static_stringD,
        variables,
        variablesA,
        expressionsA,
        conditional,
        looping,
        components,
        context,
    ]
)
def test_docs_usage(target):
    assert target.expected == target.result
