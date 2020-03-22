from viewdom.h import html, render

# start-after
name = 'viewdom'
vdom03 = html('<div>Hello {name.upper()}</div>')
result03 = render(vdom03)
