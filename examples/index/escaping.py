from viewdom import html, render

expected = '<div>&lt;span&gt;Escaping&lt;/span&gt;</div>'

# start-after
body = '<span>Escaping</span>'
result = render(html('<div>{body}</div>'))
# '<div>&lt;span&gt;Escaping&lt;/span&gt;</div>'
