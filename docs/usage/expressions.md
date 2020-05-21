# Expressions in Templates

In Python f-strings, the curly brackets can take not just variable names, but also Python "expressions".

Same is true in `viewdom`.
Let's use an expression which adds two numbers together:

```{literalinclude} ../../examples/usage/expressions.py
:end-before: end-before
```

The expression can do a bit more. For example, call a method on a string to uppercase it:

```{literalinclude} ../../examples/usage/expressionsA.py
:end-before: end-before
```

But it's Python and f-strings-ish, so you can do even more.
For example, call an in-scope function with an argument, which does some work, and insert the result:

```{literalinclude} ../../examples/usage/expressionsB.py
:end-before: end-before
```
