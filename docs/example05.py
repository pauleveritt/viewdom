from viewdom.h import html, render

# start-after

message = 'Hello'
names = ['World', 'Universe']

vdom05 = html("""
  <ul title="{message}">
    {[
        html('<li>{name}</li>')
        for name in names
     ] }
  </li>
""")
result05 = render(vdom05)
