# Static Strings

Let's start with the simplest form of templating: nothing dynamic, just "template" a string of HTML:

```{literalinclude} ../../examples/usage/static_string.py
:end-before: end-before
```


We start by importing the `html` function from `viewdom`.
This is, essentially, `htm.py` in action.
It takes a "tagged" template string and returns a VDOM.
The `render` function, imported from `vdom`, does the rendering.

Which we then do to get a result.
The rendered result matches the comment at the end.

Let's look at a variation of this, where we take the intermediate step of looking at the VDOM:

```{literalinclude} ../../examples/usage/static_stringA.py
:end-before: end-before
```

As the comment shows, we get back a Python `namedtuple` with:

- The name of the "tag" (`<div>`)

- The properties passed to that tag (in this case, an empty dict)

- The children of this tag (in this case, a text node of `Hello World`)

What would this VDOM look like if we passed in some attributes, aka "props"?

```{literalinclude} ../../examples/usage/static_stringB.py
:end-before: end-before
```

The second item in the VDOM tuple -- the props dictionary -- now has a key of 'class' with the class name value we passed in.

We can go one step further with this and use a little bit of templating.
Let's pass in a Python symbol as part of the template:

```{literalinclude} ../../examples/usage/static_stringB.py
:end-before: end-before
```

Everything is the same, except the value of the `class` prop now has a Python `int` included in the string.
If it looks like Python f-strings, well, that's the point.
We did an f-string *inside* that prop value, using a Python expression that evaluated to just the number `1`.

The VDOM's third item contains the "children".
Let's look at what more nesting would look like:

```{literalinclude} ../../examples/usage/static_stringD.py
:end-before: end-before
```
The VDOM result in the comment stretches across multiple lines and shows the nested Python data structure of these VDOMs.

The renderer also knows to collapse truthy-y values into simplified HTML attributes.
Thus, instead of `editable="1"` you just get the attribute *name* without a *value*:

```{literalinclude} ../../examples/usage/static_stringE.py
:end-before: end-before
```
