"""
Avoid passing data down long trees as props by using a Context API.
"""

from viewdom import html, render, use_context, Context

title = 'My Todos'
todos = ['first']


def Todo(label):
    prefix = use_context('prefix')
    return html('<li>{prefix}{label}</li>')


def TodoList(these_todos):
    return html('<ul>{[Todo(label) for label in these_todos]}</ul>')


result = render(
    html(
        '''
  <{Context} prefix="Item: ">
      <h1>{title}</h1>
      <{TodoList} these_todos={todos} />
  <//>
'''
    )
)
expected = '<h1>My Todos</h1><ul><li>Item: first</li></ul>'


def test():
    return expected, result
