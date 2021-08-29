"""
Subcomponents.
"""

from viewdom import html, render

title = 'My Todos'


def Todo(label):
    return html('<li>{label}</li>')


def TodoList(todos):
    return html('<ul>{[Todo(label) for label in todos]}</ul>')


def main():
    todos = ['first']
    return render(
        html(
            '''
      <h1>{title}</h1>
      <{TodoList} todos={todos} />
    '''
        )
    )


result = main()
expected = '<h1>My Todos</h1><ul><li>first</li></ul>'


def test():
    return expected, result
