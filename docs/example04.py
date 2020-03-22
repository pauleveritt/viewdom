from viewdom.h import html, render

# start-after
message = 'Say Howdy'
not_message = 'So Sad'
show_message = True

vdom04 = html("""
    <h1>Show?</h1>
    {message if show_message else not_message}
""")
result04 = render(vdom04)
