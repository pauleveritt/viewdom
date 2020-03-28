from viewdom.h import html, render

expected = '<div>Hello VIEWDOM</div>'

# start-after
name = 'viewdom'
result = render(html('<div>Hello {name.upper()}</div>'))
# '<div>Hello VIEWDOM</div>'