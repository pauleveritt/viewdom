# noinspection PyUnresolvedReferences
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
