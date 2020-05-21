from viewdom import html, render


def main(name):
    return render(html('<div>Hello {name}</div>'))


result = main(name='viewdom')
# '<div>Hello viewdom</div>'
# end-before
expected = '<div>Hello viewdom</div>'
