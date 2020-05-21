from viewdom import html, render


def main(name='viewdom'):
    return render(html('<div>Hello {name}</div>'))


result = main()
# '<div>Hello viewdom</div>'
# end-before
expected = '<div>Hello viewdom</div>'
