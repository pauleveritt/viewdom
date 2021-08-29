"""
Use normal Python syntax for conditional rendering in a template.
"""

from viewdom import html, render

message = 'Say Howdy'
not_message = 'So Sad'
show_message = True
result = render(
    html(
        '''
    <h1>Show?</h1>
    {message if show_message else not_message}
'''
    )
)
expected = '<h1>Show?</h1>Say Howdy'


def test():
    return expected, result
