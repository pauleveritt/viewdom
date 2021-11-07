# Registry and Injection

The ViewDOM component system can be used as "better templating": smaller, testable, Pythonic, re-usable units.
But it really shines when combined with Hopscotch for replaceable, injectable components.

## Simple Registered Heading

We'll start with the `Heading` component from the first components example.
In this case, our component is a dataclass, rather than a function:

```{literalinclude} ../../examples/hopscotch_app/simple_heading/app.py
---
start-at: injectable()
---
```

This time our main function simulates making a registry and processing a request:

```{literalinclude} ../../examples/hopscotch_app/simple_heading/__init__.py
---
start-at: import Heading
---
```

## Replacement

In the previous example, the component shipped with a pluggable app's package.
But a local site might want to register a replacement for that component.
Here is a `site.py` which does just this -- replace `app.Heading` with a different implementation:

```{literalinclude} ../../examples/hopscotch_app/replacement/site.py
---
start-at: injectable(
---
```

This time the decorator said `kind=Heading`.

Nothing changed in `__init__.py`, and yet, a different class was selected and `Local Site Title` is the result.
How did that work, without monkey-patching?

It's because ViewDOM can _tranparently_ look up components using a registry.
In that model, `app.Heading` isn't a dataclass.
It's a "kind"...sort of like an interface, or a base type, or a protocol.
The registry has two implementations, and the second one was added last, so it was used.

That's _replacement_.
But what if you want _both_ implementations, but used in different contexts?

## Variants

First, let's imagine our app had a concept of a `Customer`:

```{literalinclude} ../../examples/hopscotch_app/variants/app.py
---
start-after: The class used as
end-at: first_name
---
```

We could then tell our "replacement" in our local site to _only_ replace in certain cases.
Namely, when the "context" is a `Customer:`

```{literalinclude} ../../examples/hopscotch_app/variants/site.py
---
start-at: injectable(
emphasize-lines: 1
---
```

What is the "context"?
It's a special aspect of a registry.
In this case, a per-request _child registry_:

```{literalinclude} ../../examples/hopscotch_app/variants/__init__.py
---
start-at: import Custome
---
```

As you can see in the test, each "request" renders a different output:

```{literalinclude} ../../examples/hopscotch_app/variants/test_variant.py
---
start-at: assert
---
```

From a component developer's perspective, this is all transparent.
But what if I want my component to get access to that `Customer`?

## Simple Injection

We could arrange for the caller to pass in the context into the component.
But if the component is way down the component tree, it will have to be passed by all the parents.
What if the component could just ask the registry -- that is, the registry's _injector_ -- to provide the `context`

```{literalinclude} ../../examples/hopscotch_app/simple_injection/site.py
---
start-at: injectable(
emphasize-lines: 5, 9-10
---
```

Our component can then get the `first_name` off the context, because we said it was a `Customer` in the type hint.

What is `context()`?
It is a Hopscotch "operator": something which acts like a `dataclasses.field` but during injection, does extra work.
You can write your own operators, but the built-in ones have some extra features.

## Only Inject What You Need

Our component says it needs the entire `Customer`.
That's a broad surface area.
Let's change it, to ask the injector to get just the piece of information we need -- the `first_name` -- as part of injection:

```{literalinclude} ../../examples/hopscotch_app/attr/site.py
---
start-at: injectable(
emphasize-lines: 5, 9
---
```

```{note} Broke The Contract
You'll note that `app.Heading` and `site.SiteHeading` have deviated in "props".
```

This has some powerful consequences.
First, you can customize a component by passing `first_name` in manually as a prop, which will be used instead of injection.
For example, `html('<{Heading} first_name="Bob" />')`.

In a larger sense, your components could become observable.
During registration, Hopscotch could record that you need that value.
Then during injection, it could persist the `Customer` and this `SiteHeading` instance, which a relationship.
If the particular customer's `first_name` changed, you could rebuild just that component instance.
