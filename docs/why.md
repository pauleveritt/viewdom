# Why Should I Care

Of all things, templating in Python seems like the last place that a new package is needed.
We probably have newly-announced template libraries for every year going back to 1994.

Let's take a look at why something like `viewdom` might be interesting and what is its design target.

## Python Templating State of the Art

Many of the most used Python template systems and patterns come from the late 90's and early 2000's.
One purpose (in some cases, the primary) of these template systems was to isolate the HTML folks from the programming folks, to mutual benefit.

Web designers didn't need to master a full programming language nor a particular web framework.
Instead, they got an environment that was designed for their usage, simplified, and markup-oriented.
A safe zone, so to speak. What did the Python programmers get?
They got to keep the markup, as well as the web designers, out of their code.
"Separation of concerns" was the concept.

This had some negative consequences, namely: templating systems recreated facilities that were already there in Python, but in an "uncanny valley" kind of fashion.
We'll cover some more of these consequences below.

At the same time, frontend stacks such as React/JSX/Babel joyfully smashed the two back together again.
Their goal: make "components" that felt more, not less, like programming.
These components could then join in programming best practices, tooling, and reuse.

Stated differently: could you imagine trying to use a Jinja2 macro between projects?

This, in fact, is the motivation of `viewdom`: shipping an attractive, usable, modern, extensible component framework that works between different Python frameworks.

Let's look at some of the goals.

## Remove the Artificial Split

Like `htm`, this `viewdom` package quite specifically moves templating back into Python.
Want to get a symbol into your markup?
Instead of finding some magical global/local environment and context in a specific framework, just have symbols available in scope.
Want expressions?
Just use Python, same was you would in an f-string.

Want to reuse a subcomponent?
Instead of putting a macros file in some special director, just import it and use it.

Want to ship a package of components?
You know how to ship Python libraries?
It's just that.

## Less Magical

Open a template in Sphinx or a web app and try to guess where the variables come from.
Perhaps the framework has a "view" thingy that uses that template (and doesn't have any magic to get the template name) and maybe the symbol will be there.
Or not...perhaps it is in one of many layers of global "context".

"Explicit is better than implicit".
We'd like that for "templating", and we'd like to return to language constructs for symbols, expressions, scopes, conditionals, looping, and the like.
When we do so, we can then let Python teaching and Python tooling help us be more productive in large projects.

As an example, wouldn't it be great if `mypy` worked on values and expressions in "templates"?

## Modern Web

Modern frontends have set the bar much higher.
Although they do so with toolchain and complexity issues, they embrace web "applications" that try to rival native app experiences.
In particular, React's popularizing of "virtual DOMs" for high-performance dynamic updating has set an expectation of seamless site transitions.
Also, the [PRPL pattern](https://web.dev/apply-instant-loading-with-prpl) discusses a set of techniques for optimized web performance.

VDOMs, generated on the server and sent to the client, can be a way to provide a server-driven experience that still feels like the "modern web".

## Modern Patterns

The majority of modern web frontends have adopted a set of similar patterns:

- Lots of small, encapsulated components that combine into larger units
- "Props" that get passed in

It would be nice to learn from such patterns and present similar techniques for Python web development.

## Encapsulation

Look at a pixel on the screen of a Python web app.
What drew it?
With current templating approaches and "convention over configuration" with magically-named directories/files/"slots", it can be a hard question to answer.

And that's just for the markup.
What was the scope for that template?
Good luck finding that.
In the interests of a magically wonderful first five minutes experience, current templating piles stuff into a single garbage heap of scope.
Your first five minutes of hello world are great, but the next five years of real-world, not so much.

With components, nothing gets into the "template" that isn't put there by the component's scope.
Modern web systems then come up with a number of techniques -- props, state trees, context and hooks, dependency injection -- to facilitate getting state into the component.

## Customizing

Let's say you want to add something to a Sphinx sidebar, but in the space in between each panel.
Sphinx makes it easy override the sidebar template, but it has a very big surface area.
You've now forked a mini-universe.
And you are also relying on an implicit soup of state.

With a smarter component approach, you have much smaller units to change and you can register overrides for replacing a unit.


