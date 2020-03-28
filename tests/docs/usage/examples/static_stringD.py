from viewdom import html, render

vdom = html('''<div>Hello <span>World<em>!</em></span></div>''')
# H(tag='div', props={}, children=['Hello ', H(tag='span', props={}, \
# children=['World', H(tag='em', props={}, children=['!'])])])

result = render(vdom)
# '<div>Hello World</div>'
# end-before
expected = '<div>Hello <span>World<em>!</em></span></div>'
