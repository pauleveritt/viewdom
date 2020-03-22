viewdom: View Layer for Python VDOMs
====================================

``viewdom`` brings modern frontend templating patterns to Python:

- ``tagged`` to have language-centered templating
- ``htm`` to generate virtual DOM structures from a template run
- ``viewdom`` to render a VDOM to a markup string, along with other modern machinery

Quick Examples
==============

Let's look at some simple examples of various features, showing the resulting VDOM then the rendering.

Static Template
---------------

Simplest possible case: a value passed into the ``html`` function is passed all the way along to a component.

.. literalinclude:: example01.py
    :start-after: start-after

.. invisible-code-block: python

  from example01 import result01, vdom01

Our VDOM and string result in:

>>> vdom01
H(tag='div', props={}, children=['Hello World'])
>>> result01
'<div>Hello World</div>'

Data
----

We can also use data in our template, from the local scope:

.. literalinclude:: example02.py
    :start-after: start-after

.. invisible-code-block: python

  from example02 import result02, vdom02

>>> vdom02
H(tag='div', props={}, children=['Hello ', 'viewdom'])
>>> result02
'<div>Hello viewdom</div>'

Expressions
-----------

Our templates can use inline Python expressions:

.. literalinclude:: example03.py
    :start-after: start-after

.. invisible-code-block: python

  from example03 import result03, vdom03

>>> vdom03
H(tag='div', props={}, children=['Hello ', 'VIEWDOM'])
>>> result03
'<div>Hello VIEWDOM</div>'

Conditionals
------------

Conditional rendering is easy:

.. literalinclude:: example04.py
    :start-after: start-after

.. invisible-code-block: python

  from example04 import result04, vdom04

>>> vdom04
[H(tag='h1', props={}, children=['Show?']), 'Say Howdy']
>>> result04
'<h1>Show?</h1>Say Howdy'

Looping
-------

Looping is just Python:

.. literalinclude:: example05.py
    :start-after: start-after

.. invisible-code-block: python

  from example05 import result05, vdom05

>>> vdom05
H(tag='ul', props={'title': 'Hello'}, children=[[H(tag='li', props={}, children=['World']), H(tag='li', props={}, children=['Universe'])]])
>>> result05
'<ul title="Hello"><li>World</li><li>Universe</li></ul>'

Components, Props, Children, Subcomponents
------------------------------------------

We can make functions as re-usable components.
These components receive arguments as "props" and provide contained children.
These components can further subdivide into subcomponents:

.. literalinclude:: example06.py
    :start-after: start-after

.. invisible-code-block: python

  from example06 import result06

>>> result06
'<h1>My Todos</h1><ul><li>first</li></ul>'

Installation
============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

- What Is It
- Why should I care
  - Removes the artificial split
  - More Pythonic (symbols, expressions)
  - Less magical
  - Performance
  - Matches some modern frontend patterns
  - Easier to control/extend the rendering pipeline
- How it works
- Strings
- Components
- Subcomponents
- Generator components
- Context
- Custom context

Integrations

- wired
- Jinja2
- Transcrypt


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
