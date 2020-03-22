from viewdom.h import html, render

# start-after
name = 'viewdom'
vdom02 = html('<div>Hello {name}</div>')
result02 = render(vdom02)
