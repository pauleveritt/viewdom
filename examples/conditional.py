from viewdom import html, render


message = 'Say Howdy'
not_message = 'So Sad'
show_message = True
result = render(html('''
    <h1>Show?</h1>
    {message if show_message else not_message}
'''))
# '<h1>Show?</h1>Say Howdy'
# end-before
expected = '<h1>Show?</h1>Say Howdy'
