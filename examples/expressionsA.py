from viewdom import html, render


name = 'viewdom'
result = render(html('<div>Hello {name.upper()}</div>'))
# '<div>Hello VIEWDOM</div>'
# end-before
expected = '<div>Hello VIEWDOM</div>'
