from viewdom import html
from viewdom import render

vdom = html("<div editable={True}>Hello World</div>")
result = render(vdom)
expected = "<div editable>Hello World</div>"


def test():
    return expected, result
