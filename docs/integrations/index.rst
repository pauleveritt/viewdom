============
Integrations
============

A component rendering system such as ``viewdom`` makes for a nice model, but what if you have existing systems?
``viewdom`` intends to do some integrations.
Not there on all, so this is more like a roadmap.

``wired``
=========

Imagine a component system with lots of nice, well-crafted components making a pleasing UI.
Sounds great, and in fact, that's the plan.

But what if you want it to be extensible, customizable, and overridable?

``wired`` provides an interesting solution for this.
Instead of directly importing a component to use it, ``wired`` instead has a registry of component *implementations*.
You can then have multiple implementations of a ``Heading``, for different content types.
Or you can replace the use of a ``Heading`` in a particular site.
Finally, you get a safer, easier concept of ``viewdom``'s `Context`.

``Jinja``
=========

Jinja and Django templates dominate Python templating.
It would make sense to provide some integration.
For example, make it easy for a view in Flask to take advantage of components written in ``viewdom``.

At a minimum, a component tree could be rendered in the view and passed into the template, or called from within the template using an expression.
For deeper integration, significant work was done in a previous project to add a component syntax as a Jinja extension.

``Flask`` and ``Pyramid``
=========================

Beyond Jinja integration, wiring a component library into a Flask application could be made easier with some of Flask's machinery.
Ditto for Pyramid.

``Transcrypt``
==============

With ``viewdom`` you get a frontend-style component model, but server-side.
Sometimes, though, you need dynamic components that can update on the client without a server-side re-render.

`Transcrypt <https://docs.python.org/3.8/library/threading.html#thread-local-data>`_ is a Python package which transpiles Python to JavaScript, without using NodeJS.
Joachim Viide did a proof of concept of using it for a component that could render on the server in Python, then re-render on the client.
Caveats: it is tricky to work on, Transcrypt might not be the future on this topic, and the components need to keep their Python usage limited.

Client-Side ``htm``
===================

Joachim has another server-side/client-side demo that is more realistic: use the server to generate VDOM data structures which are sent to the client for rendering in an existing view layer.
With this, your Python stays on the server.
It does mean, though, that all interactions require a trip to the server.