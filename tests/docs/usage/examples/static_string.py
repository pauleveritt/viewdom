from viewdom import html, render

result = render(html('''<div>Hello World</div>'''))
# '<div>Hello World</div>'
# end-before
expected = '<div>Hello World</div>'
