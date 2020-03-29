from viewdom import html, render

vdom = html('''<div editable={True}>Hello World</div>''')
# H(tag='div', props={'editable': True}, children=['Hello World'])

result = render(vdom)
# '<div editable>Hello World</div>'
# end-before
expected = '<div editable>Hello World</div>'
