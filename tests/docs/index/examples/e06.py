from viewdom.h import html, render

expected = '<h1>My Todos</h1><ul><li>first</li></ul>'

# start-after
title = 'My Todos'
todos = ['first']


def Todo(label):
    return html('<li>{label}</li>')


def TodoList(todos):
    return html('<ul>{[Todo(label) for label in todos]}</ul>')


result = render(html('''
  <h1>{title}</h1>
  <{TodoList} todos={todos} />
'''))
