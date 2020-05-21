from viewdom import html, render


def Heading(children):
    return html('<h1>My Title</h1><div>{children}</div>')


result = render(html('<{Heading} >Hi<//>'))
# '<h1>My Title</h1><div>Hi</div>'
# end-before
expected = '<h1>My Title</h1><div>Hi</div>'
