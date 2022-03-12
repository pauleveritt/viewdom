# ViewDOM: Component-Driven Development for Python

[![Coverage Status][codecov-badge]][codecov-link]
[![Documentation Status][rtd-badge]][rtd-link]
[![Code style: black][black-badge]][black-link]
[![PyPI][pypi-badge]][pypi-link]
[![Python Version][pypi-badge]][pypi-link]
[![PyPI - Downloads][install-badge]][install-link]
[![License][license-badge]][license-link]
[![Test Status][tests-badge]][tests-link]
[![pre-commit][pre-commit-badge]][pre-commit-link]
[![black][black-badge]][black-link]

[codecov-badge]: https://codecov.io/gh/pauleveritt/viewdom/branch/main/graph/badge.svg
[codecov-link]: https://codecov.io/gh/pauleveritt/viewdom
[rtd-badge]: https://readthedocs.org/projects/viewdom/badge/?version=latest
[rtd-link]: https://viewdom.readthedocs.io/en/latest/?badge=latest
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-link]: https://github.com/ambv/black
[pypi-badge]: https://img.shields.io/pypi/v/viewdom.svg
[pypi-link]: https://pypi.org/project/viewdom
[install-badge]: https://img.shields.io/pypi/dw/viewdom?label=pypi%20installs
[install-link]: https://pypistats.org/packages/viewdom
[license-badge]: https://img.shields.io/pypi/l/viewdom
[license-link]: https://opensource.org/licenses/MIT
[tests-badge]: https://github.com/pauleveritt/viewdom/workflows/Tests/badge.svg
[tests-link]: https://github.com/pauleveritt/viewdom/actions?workflow=Tests
[pre-commit-badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-link]: https://github.com/pre-commit/pre-commit

ViewDOM brings modern frontend templating patterns to Python:

- [tagged](https://github.com/jviide/tagged) to have language-centered templating (like JS tagged templates)
- [htm](https://github.com/jviide/htm.py) to generate virtual DOM structures from a template run (like the `htm` JS package)
- ViewDOM for components which render a VDOM to a markup string, along with other modern machinery
- Optionally, [Hopscotch](https://github.com/pauleveritt/hopscotch) for a component registry with dependency injection

## Features

- Component-driven development.
- Intermediate VDOM.
- Pass in data either via props (simple) or DI (rich).
- Emphasis on modern Python dev practices: explicit, type hinting,
  static analysis, testing, docs, linting, editors.

## Requirements

- Python 3.9+.
- viewdom
- tagged
- htm.py
- Markupsafe

## Installation

You can install ViewDOM via [pip](https://pip.pypa.io/) from [PyPI](https://pypi.org/):

```shell
$ pip install viewdom
```

# Quick Examples

Use ``htm`` to generate a VDOM, then ``render`` to convert to a string:

```python
render(html("<div>Hello World</div>"))
```

If you'd like, you can split those into two steps:

```python
vdom = html("<div>Hello World</div>")
render(vdom)
```

Insert variables from the normal Python local or global scope:

```python
name = "viewdom"
render(html("<div>Hello {name}</div>"))
```

Expressions aren't some special language, it's just Python in inside curly braces:

```python
name = "viewdom"
render(html("<div>Hello {name.upper()}</div>"))
```

Rendering something conditionally is also "just Python":

```python
message = "Say Howdy"
not_message = "So Sad"
show_message = True
render(html("""
    <h1>Show?</h1>
    {message if show_message else not_message}
  """))
```

Looping? Yes, "just Python":

```python
message = "Hello"
names = ["World", "Universe"]

render(
    html(
        """
  <ul title="{message}">
    {[
        html('<li>{name}</li>')
        for name in names
     ] }
  </li>
"""
    )
)
```

Reusable components and subcomponents, passing props and children:

```python
def Todo(label):
    """Render a to do."""
    return html("<li>{label}</li>")


def TodoList(todos):
    """Render a list of to dos."""
    return html("<ul>{[Todo(label) for label in todos]}</ul>")


title = "My Todos"
todos = ["first"]

render(
    html(
        """
  <h1>{title}</h1>
  <{TodoList} todos={todos} />
"""
    )
)
```
Components can be any kind of callable:

```python
@dataclass
class Greeting:
    """Give a greeting."""

    name: str

    def __call__(self):
        """Render to a string."""
        return f"Hello {self.name}"

greeting = Greeting(name="viewdom")
render(html("<div><{greeting} /></div>"))
```

Tired of passing props down a deep tree and want something like React context/hooks?

```python

def Todo(label):
    """Render a to do."""
    prefix = use_context("prefix")
    return html("<li>{prefix}{label}</li>")


def TodoList(these_todos):
    """Render a to do list."""
    return html("<ul>{[Todo(label) for label in these_todos]}</ul>")


title = "My Todos"
todos = ["first"]
render(
    html(
        """
  <{Context} prefix="Item: ">
      <h1>{title}</h1>
      <{TodoList} these_todos={todos} />
  <//>
"""
    )
)
```


# Contributing

Contributions are very welcome.
To learn more, see the [contributor's guide](contributing).

# License

Distributed under the terms of the [MIT license](https://opensource.org/licenses/MIT), ViewDOM is free and open source software.

# Issues

If you encounter any problems,
please [file an issue](https://github.com/pauleveritt/viewdom/issues) along with a detailed description.

# Credits

This project was generated from [@cjolowicz's](https://github.com/cjolowicz) [Hypermodern Python Cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python) template.
