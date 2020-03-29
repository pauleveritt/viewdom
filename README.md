# viewdom

[Docs](https://viewdom.readthedocs.io/en/latest/) and [Code](https://github.com/pauleveritt/viewdom)


`viewdom` brings modern frontend templating patterns to Python:

- [tagged](https://github.com/jviide/tagged) to have language-centered templating (like JS tagged templates)
- [htm](https://github.com/jviide/htm.py) to generate virtual DOM structures from a template run (like the `htm` JS package)
- `viewdom` to render a VDOM to a markup string, along with other modern machinery

# Installation

Installation follows the normal Python packaging:

``shell script

  $ pip install viewdom
``

*Note: `viewdom` depends on `htm` which depends on `tagged`.
No other dependencies, although some of the optional `viewdom` integrations pull in other packages.`

# Quick Examples

Use `html` to generate a VDOM, then `render` to convert to a string:

```python
result = render(html('''<div>Hello World</div>'''))
# '<div>Hello World</div>'
```

If you'd like, you can split those into two steps:

```python
vdom = html('''<div>Hello World</div>''')
result = render(vdom)
# '<div>Hello World</div>'
```

Insert variables from the local or global scope:

```python
name = 'viewdom'
result = render(html('<div>Hello {name}</div>'))
# '<div>Hello viewdom</div>'
```

Expressions aren't some special language, it's just Python in inside curly braces:

```python
name = 'viewdom'
result = render(html('<div>Hello {name.upper()}</div>'))
# '<div>Hello VIEWDOM</div>'
```

.. literalinclude:: ../tests/docs/index/examples/e03.py
    :start-after: start-after

Rendering something conditionally is also "just Python":

```python
message = 'Say Howdy'
not_message = 'So Sad'
show_message = True
result = render(html('''
    <h1>Show?</h1>
    {message if show_message else not_message}
'''))
# '<h1>Show?</h1>Say Howdy'
```

Looping? Yes, "just Python":

```python
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
```

Reusable components and subcomponents, passing props and children:

```python
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
# '<h1>My Todos</h1><ul><li>first</li></ul>'
```

Tired of passing props down a deep tree and want something like React context/hooks?

```python
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
```

# Acknowledgments

The idea and code for `viewdom` -- the rendering, the idea of a theadlocal context, obviously `tagged` and `htm`... essentially everything -- come from [Joachim Viide](https://github.com/jviide).