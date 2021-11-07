# Registry and Injection

The ViewDOM component system can be used as "better templating": smaller, testable, Pythonic, re-usable units.
But it really shines when combined with Hopscotch for replaceable, injectable components.

## Simple Registered Heading

We'll start with the `Heading` component from the first components example.
In this case, our component is a dataclass, rather than a function.

```{literalinclude} ../../examples/hopscotch_app//components.py
---
---
```

This time our main function simulates making an app and processing a request:


```{literalinclude} ../../examples/hopscotch_app//components.py
---
---
```
