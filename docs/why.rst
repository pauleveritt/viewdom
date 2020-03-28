=================
Why Should I Care
=================

Of all things, templating in Python seems like the last place that a new package is needed.
We probably have newly-announced template libraries for every year going back to 1994.

Let's take a look at why something like ``viewdom`` might be interesting and what is its design target.

Python Templating State of the Art
==================================

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

This, in fact, is the motivation of ``viewdom``: shipping an attractive, usable, modern, extensible component framework that works between different Python frameworks.

Let's look at some of the goals.

Remove the Artificial Split
===========================

Like ``htm``, this ``viewdom`` package quite specifically moves templating back into Python.
Want to get a symbol into your markup?
Instead of finding some magical global/local environment and context in a specific framework, just have symbols available in scope.
Want expressions?
Just use Python, same was you would in an f-string.

Want to reuse a subcomponent?
Instead of putting a macros file in some special director, just import it and use it.

Want to ship a package of components?
You know how to ship Python libraries?
It's just that.

Less Magical
============

Open a template in Sphinx or a web app and try to guess where the variables come from.
Perhaps the framework has a "view" thingy that uses that template (and doesn't have any magic to get the template name) and maybe the symbol will be there.
Or not...perhaps it is in one of many layers of global context.



- More Pythonic (symbols, expressions)
- Less magical
- Performance
- Matches some modern frontend patterns
- Isolation
- Different ways to get state in
- Fresh thinking
- Easier to control/extend the rendering pipeline

