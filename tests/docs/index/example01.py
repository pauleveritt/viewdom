from viewdom.h import html, render

expected = '<div>Hello World</div>'

# start-after
result = render(html('''<div>Hello World</div>'''))
# '<div>Hello World</div>'
