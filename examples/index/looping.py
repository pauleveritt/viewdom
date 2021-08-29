"""
Loop over a sequence and generate nodes.
"""

from viewdom import html, render

message = 'Hello'
names = ['World', 'Universe']

result = render(
    html(
        '''
  <ul title="{message}">
    {[
        html('<li>{name}</li>')
        for name in names
     ] }
  </li>
'''
    )
)
expected = '<ul title="Hello"><li>World</li><li>Universe</li></ul>'


def test():
    return expected, result
