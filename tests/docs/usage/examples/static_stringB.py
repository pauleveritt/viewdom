from viewdom import html, render

vdom = html('''<div class="container">Hello World</div>''')
# H(tag='div', props={'class': 'container'}, children=['Hello World'])

result = render(vdom)
# '<div class="container">Hello World</div>'
# end-before
expected = '<div class="container">Hello World</div>'
