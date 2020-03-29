from viewdom import html, render


def Heading(children, title):
    return html('<h1>{title}</h1><div>{children}</div>')


result = render(html('<{Heading} title="My Title">Child<//>'))
# '<h1>My Title</h1><div>Child</div>'
# end-before
expected = '<h1>My Title</h1><div>Child</div>'
