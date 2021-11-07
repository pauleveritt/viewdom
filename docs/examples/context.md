# Context

When you really embrace components and subcomponents, you end up with deeply nested component trees.
It can be frustrating, not to mention brittle, to pass data all the way from the top to the bottom.
Intermediate components don't use the data.
Why should they have to depend on them?

## Pass-Through

This is the harder, manual way.

In this example the `site` object is passed through the `App` component, then `Nav`, to get it to `NavHeading`.
Neither `App` nor `Nav` need anything from `site`.
They are just transits.

```{literalinclude} ../../examples/context/nested_context/__init__.py
---
start-at: def NavHeading
---
```

## Context

This is the easier way.

React has addressed this with a number of technologies over the years, including [Context](https://reactjs.org/docs/context.html) and [Hooks](https://reactjs.org/docs/hooks-intro.html).
`viewdom` has a similar "context" construct, where you can wrap a part of the component tree, shove values into the rendering, and pluck them out later on.
We can use this to make `site` available anywhere in the tree:

```{literalinclude} ../../examples/context/context_api/__init__.py
---
start-at: def NavHeading
---
```

As you can imagine, a React Hooks approach could also be implemented.
