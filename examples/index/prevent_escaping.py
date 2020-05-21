from markupsafe import Markup
from viewdom import html, render

expected = '<div><span>No Escaping</span></div>'

# start-after
body = Markup('<span>No Escaping</span>')
result = render(html('<div>{body}</div>'))
# '<div><span>No Escaping</span></div>'
