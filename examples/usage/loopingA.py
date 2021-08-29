from viewdom import html, render

message = 'Hello'
names = ['World', 'Universe']
items = [html('<li>{label}</li>') for label in names]
result = render(
    html(
        '''
  <ul title="{message}">
    {items}
  </li>
'''
    )
)
expected = '<ul title="Hello"><li>World</li><li>Universe</li></ul>'


def test():
    return expected, result
