from viewdom import html, render
from .variables import name


def main():
    return render(html('<div>Hello {name}</div>'))


result = main()
# '<div>Hello viewdom</div>'
# end-before
expected = '<div>Hello viewdom</div>'
