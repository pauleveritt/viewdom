# Context

When you really embrace components and subcomponents, you end up with deeply nested component trees.
It can be frustrating, not to mention brittle, to pass data all the way from the top to the bottom.
Intermediate components don't use the data.
Why should they have to depend on them?

```{literalinclude} ../../examples/usage/context.py
:end-before: end-before
```

In this example the `site` object is passed through the `App` component, then `Nav`, to get it to `NavHeading`.
Neither `App` nor `Nav` need anything from `site`.
They are just transits.

React has addressed this with a number of technologies over the years, including [Context](https://reactjs.org/docs/context.html) and [Hooks](https://reactjs.org/docs/hooks-intro.html).
`viewdom` has a similar "context" construct, where you can wrap a part of the component tree, shove values into the rendering, and pluck them out later on.
We can use this to make `site` available anywhere in the tree:

```{literalinclude} ../../examples/usage/contextA.py
:end-before: end-before
```

## How It Works

The `Context` in `viewdom` seems to violate scope.
There isn't a global (which is good).
But values and state seem to magically appear in other scopes.
Where is this state stored and retrieved?

`Context` uses [thread-local data](https://docs.python.org/3.8/library/threading.html#thread-local-data) which is a Python system for storing data in a thread and making it accessible to anything that grabs it.
It's generally considered "iffy" on the meter of good practices.
When used narrowly, it can be considered safe.