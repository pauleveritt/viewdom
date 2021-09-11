import pytest
from examples.readme import callable
from examples.readme import components
from examples.readme import conditional
from examples.readme import context
from examples.readme import escaping
from examples.readme import expressions
from examples.readme import looping
from examples.readme import prevent_escaping
from examples.readme import props
from examples.readme import render
from examples.readme import scope
from examples.readme import split
from examples.readme import vdom
from examples.usage import components as usage_components
from examples.usage import components_vdom
from examples.usage import componentsA
from examples.usage import componentsB
from examples.usage import componentsC
from examples.usage import componentsD
from examples.usage import componentsE
from examples.usage import componentsF
from examples.usage import componentsG
from examples.usage import componentsH
from examples.usage import componentsI
from examples.usage import componentsJ
from examples.usage import componentsPassComponent
from examples.usage import componentsPassComponentB
from examples.usage import componentsPassComponentC
from examples.usage import conditional as usage_conditional
from examples.usage import context as usage_context
from examples.usage import contextA
from examples.usage import expressions as usage_expressions
from examples.usage import expressionsA
from examples.usage import expressionsB
from examples.usage import looping as usage_looping
from examples.usage import loopingA
from examples.usage import spread
from examples.usage import static_string
from examples.usage import static_stringB
from examples.usage import static_stringC
from examples.usage import static_stringC2
from examples.usage import static_stringD
from examples.usage import static_stringDoctype
from examples.usage import static_stringE
from examples.usage import static_stringLiteral
from examples.usage import variables
from examples.usage import variablesA
from examples.usage import variablesB
from examples.usage import variablesC
from examples.usage import variablesD


@pytest.mark.parametrize(
    "target",
    [
        vdom,
        render,
        split,
        scope,
        props,
        expressions,
        escaping,
        prevent_escaping,
        expressions,
        conditional,
        looping,
        components,
        callable,
        context,
        static_string,
        static_stringLiteral,
        static_stringB,
        static_stringC,
        static_stringC2,
        static_stringD,
        static_stringE,
        static_stringDoctype,
        variables,
        variablesA,
        variablesB,
        variablesC,
        variablesD,
        usage_expressions,
        expressionsA,
        expressionsB,
        usage_conditional,
        usage_looping,
        loopingA,
        usage_components,
        components_vdom,
        componentsA,
        componentsB,
        componentsC,
        componentsD,
        componentsE,
        componentsPassComponent,
        componentsPassComponentB,
        componentsPassComponentC,
        componentsF,
        componentsG,
        componentsH,
        componentsI,
        componentsJ,
        usage_context,
        contextA,
        spread,
    ],
)
def test_examples(target):
    expected, actual = target.test()
    assert expected == actual
