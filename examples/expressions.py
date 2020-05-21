from viewdom import html, render


name = 'viewdom'
result = render(html('<div>Hello {1 + 3}</div>'))
# '<div>Hello 4</div>'
# end-before
expected = '<div>Hello 4</div>'
