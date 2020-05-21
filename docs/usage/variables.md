# Insert Variables

Inserting a variable into a template mimics what you would expect from a Python f-string.

For example, in this case there is only one scope, the global one:

```{literalinclude} ../../examples/usage/variables.py
:end-before: end-before
```

But in this case, the template is in a function, and `name` comes from that scope:

```{literalinclude} ../../examples/usage/variablesA.py
:end-before: end-before
```

In this third case, `name` is imported from another module:

```{literalinclude} ../../examples/usage/variablesB.py
:end-before: end-before
```

Of course, the function could get the symbol as an argument:

```{literalinclude} ../../examples/usage/variablesC.py
:end-before: end-before
```

The function could make passing the argument optional by providing a default:

```{literalinclude} ../../examples/usage/variablesD.py
:end-before: end-before
```

What's the moral of the story?
No new template rules for variables and scope, just stuff you would expect from Python.
