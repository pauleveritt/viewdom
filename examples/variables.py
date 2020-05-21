from viewdom import html, render

name = 'viewdom'
result = render(html('<div>Hello {name}</div>'))

# '<div>Hello viewdom</div>'
# end-before
expected = '<div>Hello viewdom</div>'
