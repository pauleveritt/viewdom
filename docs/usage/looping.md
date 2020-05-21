# Looping

It's common in templating to format a list of items, for example, a `<ul>` list.
Many Python template languages invent a Python-like grammar to do `for` loops and the like.

You know what's more Python-like?
Python.
f-strings can do looping in a Python expression using list comprehensions and so can `viewdom`:

```{literalinclude} ../../examples/usage/looping.py
:end-before: end-before
```

You could also move the generation of the items out of the "parent" template, then use that VDOM result in the next template:

```{literalinclude} ../../examples/usage/loopingA.py
:end-before: end-before
```

