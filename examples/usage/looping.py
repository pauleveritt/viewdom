from viewdom import html, render

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
# '<ul title="Hello"><li>World</li><li>Universe</li></ul>'
# end-before
expected = '<ul title="Hello"><li>World</li><li>Universe</li></ul>'
