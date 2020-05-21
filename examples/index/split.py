from viewdom import html, render

expected = '<div>Hello World</div>'

# start-after
vdom = html('''<div>Hello World</div>''')
result = render(vdom)
# '<div>Hello World</div>'
