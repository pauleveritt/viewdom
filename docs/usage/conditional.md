# Conditional Templating

It's a common pattern in templating: return one chunk of HTML most of the time, but under certain conditions, return a different chunk.

Thus, conditionals are a common part of templating.
They're also a common part of Python f-strings, because...well, Python has conditionals.
Here's a simple example using a Python "ternary":

```{literalinclude} ../../examples/usage/conditional.py
:end-before: end-before
```
