from viewdom import html, render


def Todos():
    for todo in ["First", "Second"]:
        yield html('<li>{todo}</li>')


result = render(html('<ul><{Todos}/></ul>'))
# '<ul><li>First</li><li>Second</li></ul>'
# end-before
expected = '<ul><li>First</li><li>Second</li></ul>'
