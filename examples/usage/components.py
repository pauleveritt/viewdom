from viewdom import html, render


def Heading():
    return html('<h1>My Title</h1>')


vdom = html('<{Heading} />')
# H(tag=<function Heading at 0x10e77db80>, props={}, children=[])
result = render(vdom)
# '<h1>My Title</h1>'
# end-before
expected = '<h1>My Title</h1>'
