from viewdom import html, render

expected = '<div>Hello viewdom</div>'

# start-after
name = 'viewdom'
result = render(html('<div>Hello {name}</div>'))
# '<div>Hello viewdom</div>'
