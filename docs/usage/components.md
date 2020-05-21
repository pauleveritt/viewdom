# Components

You often have a snippet of templating that you'd like to re-use.
Many existing templating systems have "macros" for this: units of templating that can be re-used and called from other templates.

The whole mechanism, though, is quite magical:

- Where do the macros come from?
  Multiple layers of context magic and specially-named directories provide the answer.

- What macros are avaiable at the cursor position I'm at in a template?
  It's hard for an editor or IDE to predict and provide autocomplete.

- What are the macros arguments and what is this template's special syntax for providing them?
  And can my editor help on autocomplete or telling me when I got it wrong (or the macro changed its signature)?

- How does my current scope interact with the macro's scope, and where does it get other parts of its scope from?

`viewdom`, courtesy of `htm.py`, makes this more Pythonic through the use of "components".
Instead of some sorta-callable, a component is a normal Python callable -- e.g. a function -- with normal Python arguments and return values.

```{literalinclude} ../../examples/usage/components.py
:end-before: end-before
```

As you can see from the comment, the VDOM now has something special in it: a VDOM with callable function `Heading` and props/children, rather than the rendering.

If your template has children inside that tag, your component can ask for them as an argument, then place them as a variable:

```{literalinclude} ../../examples/usage/componentsA.py
:end-before: end-before
```

Note how the component closes with `<//>` when it contains nested children, as opposed to the self-closing form in the first example.

As expected, components can have props, passed as what looks like HTML attributes.
Here we pass a `title` as an argument to `Heading`, using a simple HTML attribute string value:

The "prop" can also be a Python symbol, using curly braces as the attribute value:

```{literalinclude} ../../examples/usage/componentsC.py
:end-before: end-before
```

That prop value can also be an in-scope variable:

```{literalinclude} ../../examples/usage/componentsD.py
:end-before: end-before
```

Since this is typical function-argument stuff, you can have optional props through argument defaults:

```{literalinclude} ../../examples/usage/componentsE.py
:end-before: end-before
```

You can combined different props and arguments.
In this case, `title` is a prop.
`children` is another argument, but is provided automatically by `render`.

```{literalinclude} ../../examples/usage/componentsF.py
:end-before: end-before
```

You can also have components that act as generators.
For example, imagine you have a todo list.
There might be a lot of todos, so you want to generate them in a memory-efficient way:

```{literalinclude} ../../examples/usage/componentsG.py
:end-before: end-before
```

Subcomponents are also feasible.
They make up part of both the VDOM and the rendering:

```{literalinclude} ../../examples/usage/componentsH.py
:end-before: end-before
```

Architectural Note
==================

Components and subcomponents are a useful feature to users of some UI layer, as well as creators of that layer.
They are also, though, an interesting architectural plug point.

As `render` walks through a VDOM, a usage of a component pops up with the props and children.
But it isn't yet the *rendered* component.
The callable...hasn't been called.

It's the job of `render` to do so.
If you look at the code for `render` and the utilities it uses, it's not a lot of code.
It's reasonable to write your own, which is what some of the integrations have done.

This becomes an interesting place to experiment with your own component policies.
Want a cache layer?
Want to log each call?
Maybe type validation?
Want to (like the `wired` integration) write a custom DI system that gets argument values from special locations (e.g. database queries)?

Lots of possibilities, especially since the surface area is small enough and easy enough to play around.
