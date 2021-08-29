from viewdom import html, render

vdom = html('<div editable={True}>Hello World</div>')
result = render(vdom)
expected = '<div editable>Hello World</div>'


def test():
    return expected, result
