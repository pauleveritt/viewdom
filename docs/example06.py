from viewdom.h import html, render

# start-after
title = 'My Todos'
todos = ['first']


def Todo(label):
    return html('''<li>{label}</li>''')


def TodoList(todos):
    return html('''<ul>{[Todo(label) for label in todos]}</ul>''')


vdom06 = html("""
  <h1>{title}</h1>
  <{TodoList} todos={todos} />
""")
result06 = render(vdom06)
