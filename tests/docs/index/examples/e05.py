from viewdom.h import html, render

expected = '<ul title="Hello"><li>World</li><li>Universe</li></ul>'

# start-after
message = 'Hello'
names = ['World', 'Universe']
result = render(html('''
  <ul title="{message}">
    {[
        html('<li>{name}</li>')
        for name in names
     ] }
  </li>
'''))
