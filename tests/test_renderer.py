"""Test rendering."""
import pytest
from markupsafe import Markup

from viewdom import html
from viewdom import render
from viewdom import use_context


def functional_component(children, header="Functional components!"):
    """Make a functional component."""
    message = use_context("message")  # noqa

    return html(
        """
        <h2>{header}</h2>
        <span>{message}</span>
        {children}
    """
    )


def test_single_renderer():
    """Test just one div."""
    vdom = html('<div id="d1">div1</div>')
    assert ["div1"] == vdom.children


def test_double_renderer():
    """Test two sibling divs."""
    vdom = html('<div id="d1">div1</div><div id="d2">div2</div>')
    assert ["div1"] == vdom[0].children
    assert ["div2"] == vdom[1].children


@pytest.mark.skip(reason="Implementation was removed.")
def test_render_context():
    """Test the context support."""
    from viewdom import Context  # noqa

    def App():  # noqa
        message = use_context("message")  # noqa
        return html("<div>{message}<//><{functional_component}/>")

    vdom = html(
        """
  <{Context} message='c1'>
    <{App} />
  <//>
"""
    )
    result = render(vdom)
    expected = "<div>c1</div><h2>Functional components!</h2><span>c1</span>"
    assert expected == result


def test_render_escaped_value():
    """Handle escaped values."""
    body = "<span>Escape</span>"  # noqa
    vdom = html("<div>{body}</div>")
    result = render(vdom)
    expected = "<div>&lt;span&gt;Escape&lt;/span&gt;</div>"
    assert expected == result


def test_render_safe_value():
    """Support markup safe."""
    body = Markup("<span>Escape</span>")  # noqa
    vdom = html("<div>{body}</div>")
    result = render(vdom)
    expected = "<div><span>Escape</span></div>"
    assert expected == result


def test_void():
    """Convert <img></img> to <img/>.

    See this for discussion of non-void elements which can't be
    self-closed:
    https://stackoverflow.com/questions/31627593/html-validator-self-closing-syntax-and-non-void-errors
    """  # noqa B950
    non_void = "<img></img>"
    vdom = html(non_void)
    result = render(vdom)
    assert "<img/>" == result


def test_non_void():
    """Don't convert <i class="icon"></i> to <i class="icon"/>.

    See this for discussion of non-void elements which can't be
    self-closed:
    https://stackoverflow.com/questions/31627593/html-validator-self-closing-syntax-and-non-void-errors
    """  # noqa B950

    non_void = '<i class="icon"></i>'
    vdom = html(non_void)
    result = render(vdom)
    assert non_void == result
