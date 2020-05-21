from markupsafe import Markup
from viewdom.h import Context, use_context, html, render


def functional_component(children, header="Functional components!"):
    message = use_context("message")

    return html("""
        <h2>{header}</h2>
        <span>{message}</span>
        {children}
    """)


def test_render_context():

    def App():
        message = use_context("message")
        return html("<div>{message}<//><{functional_component}/>")

    vdom = html("""
  <{Context} message='c1'>
    <{App} />
  <//>
""")
    result = render(vdom)
    expected = '<div>c1</div><h2>Functional components!</h2><span>c1</span>'
    assert result == expected


def test_render_escaped_value():
    body = '<span>Escape</span>'
    vdom = html('<div>{body}</div>')
    result = render(vdom)
    expected = '<div>&lt;span&gt;Escape&lt;/span&gt;</div>'
    assert result == expected


def test_render_safe_value():
    body = Markup('<span>Escape</span>')
    vdom = html('<div>{body}</div>')
    result = render(vdom)
    expected = '<div><span>Escape</span></div>'
    assert result == expected
