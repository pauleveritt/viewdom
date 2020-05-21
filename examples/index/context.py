from viewdom import html, render, use_context, Context

expected = '<h1>My Todos</h1><ul><li>Item: first</li></ul>'

# start-after
title = 'My Todos'
todos = ['first']


def Todo(label):
    prefix = use_context('prefix')
    return html('<li>{prefix}{label}</li>')


def TodoList(todos):
    return html('<ul>{[Todo(label) for label in todos]}</ul>')


result = render(html('''
  <{Context} prefix="Item: ">
      <h1>{title}</h1>
      <{TodoList} todos={todos} />
  <//>    
'''))
# '<h1>My Todos</h1><ul><li>Item: first</li></ul>'
