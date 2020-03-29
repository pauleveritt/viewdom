viewdom: View Layer for Python VDOMs
====================================

``viewdom`` brings modern frontend templating patterns to Python:

- `tagged <https://github.com/jviide/tagged>`_ to have language-centered templating (like JS tagged templates)
- `htm <https://github.com/jviide/htm.py>`_ to generate virtual DOM structures from a template run (like the ``htm`` JS package)
- ``viewdom`` to render a VDOM to a markup string, along with other modern machinery

Installation
============

Installation follows the normal Python packaging approach:

.. code-block:: bash

  $ pip install viewdom

.. note::
    ``viewdom`` depends on ``htm`` which depends on ``tagged``.
    No other dependencies, although some of the optional ``viewdom`` :doc:`integrations <./integrations/index>` pull in other packages.

Quick Examples
==============

Use ``html`` to generate a VDOM, then ``render`` to convert to a string:

.. literalinclude:: ../tests/docs/index/examples/e01.py
    :start-after: start-after

If you'd like, you can split those into two steps:

.. literalinclude:: ../tests/docs/index/examples/e01a.py
    :start-after: start-after

Insert variables from the local or global scope:

.. literalinclude:: ../tests/docs/index/examples/e02.py
    :start-after: start-after

Expressions aren't some special language, it's just Python in inside curly braces:

.. literalinclude:: ../tests/docs/index/examples/e03.py
    :start-after: start-after

Rendering something conditionally is also "just Python":

.. literalinclude:: ../tests/docs/index/examples/e04.py
    :start-after: start-after

Looping? Yes, "just Python":

.. literalinclude:: ../tests/docs/index/examples/e05.py
    :start-after: start-after

Reusable components and subcomponents, passing props and children:

.. literalinclude:: ../tests/docs/index/examples/e06.py
    :start-after: start-after

Tired of passing props down a deep tree and want something like React context/hooks?

.. literalinclude:: ../tests/docs/index/examples/e07.py
    :start-after: start-after

Acknowledgments
===============

The idea and code for ``viewdom`` -- the rendering, the idea of a theadlocal context, obviously ``tagged`` and ``htm``... essentially everything -- come from `Joachim Viide <https://github.com/jviide>`_.

.. toctree::
    :hidden:

    what
    why
    how
    usage/index
    integrations/index
