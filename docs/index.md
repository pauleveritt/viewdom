# viewdom: View Layer for Python VDOMs

`viewdom` brings modern frontend templating patterns to Python:

- [tagged](https://github.com/jviide/tagged) to have language-centered templating (like JS tagged templates)
- [htm](https://github.com/jviide/htm.py) to generate virtual DOM structures from a template run (like the `htm` JS package)
- `viewdom` to render a VDOM to a markup string, along with other modern machinery

## Installation

Installation follows the normal Python packaging approach:

```bash
  $ pip install viewdom
```

```{note}
`viewdom` depends on `htm` which depends on `tagged` which depends on nothing.
```

## Quick Examples

Use `html` to generate a VDOM, then `render` to convert to a string:

```{literalinclude} ../examples/index/e01.py
```

If you'd like, you can split those into two steps:

```{literalinclude} ../examples/index/e01a.py
```

Insert variables from the local or global scope:

```{literalinclude} ../examples/index/e02.py
```

Expressions aren't some special language, it's just Python in inside curly braces:

```{literalinclude} ../examples/index/e03.py
```

Rendering something conditionally is also "just Python":

```{literalinclude} ../examples/index/e04.py
```

Looping? Yes, "just Python":

```{literalinclude} ../examples/index/e05.py
```

Reusable components and subcomponents, passing props and children:

```{literalinclude} ../examples/index/e06.py
```

Tired of passing props down a deep tree and want something like React context/hooks?

```{literalinclude} ../examples/index/e07.py
```

## Acknowledgments

The idea and code for `viewdom` -- the rendering, the idea of a theadlocal context, obviously `tagged` and `htm` --- essentially everything -- come from [Joachim Viide](https://github.com/jviide).

```{toctree}
---
hidden: true
---
what
why
how
usage/index
```
