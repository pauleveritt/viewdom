"""ViewDOM."""
from __future__ import annotations

import functools
import threading
from collections import ChainMap
from collections.abc import ByteString
from collections.abc import Iterable
from dataclasses import dataclass
from typing import Callable
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union

from hopscotch import Registry
from hopscotch.registry import inject_callable
from hopscotch.registry import Props
from hopscotch.registry import Registration
from htm import htm_eval
from htm import htm_parse
from markupsafe import escape
from tagged import tag

# "void" elements are allowed to be self-closing
# https://html.spec.whatwg.org/multipage/syntax.html#void-elements
VOIDS = (
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "keygen",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
)


@dataclass(frozen=True)
class VDOMNode:
    """Implementation of a node with three slots."""

    __slots__ = ["tag", "props", "children"]
    tag: str
    props: Mapping
    children: List[Union[str, VDOMNode]]


VDOM = Union[Sequence[VDOMNode], VDOMNode]


def htm(func=None, *, cache_maxsize=128) -> Callable[[str], VDOM]:
    """The callable function to act as decorator."""
    cached_parse = functools.lru_cache(maxsize=cache_maxsize)(htm_parse)

    def _htm(h):
        @tag
        @functools.wraps(h)
        def __htm(strings, values):
            ops = cached_parse(strings)
            return htm_eval(h, ops, values)

        return __htm

    if func is not None:
        return _htm(func)
    return _htm


html = htm(VDOMNode)


def flatten(value):
    """Reduce a sequence."""
    if isinstance(value, Iterable) and not isinstance(
        value, (VDOMNode, str, ByteString)
    ):
        for item in value:
            yield from flatten(item)
    elif callable(value):
        # E.g. a dataclass with an __call__
        vdom = value()
        yield vdom
    else:
        yield value


def relaxed_call(
    callable_,
    registry: Optional[Registry] = None,
    children=None,
    props: Optional[Props] = None,
) -> VDOM:
    """Get the correct implementation and call it to produce a vdom."""
    # Props should include children, which come from "the system"
    if props is None:
        props = {}
    full_props = props | dict(children=children)

    vdom = None
    if registry:
        # Try to get the implementation from the registry.
        try:
            vdom = registry.get(callable_, **full_props)
        except LookupError:
            # We'll give a chance at the next step.
            pass
    # We can still use plain-old-symbol unregistered callables when
    # using a registry, so if not found, use it directly.
    if vdom is None:
        if callable_.__class__.__name__ not in ["type", "function"] and callable(
            callable_
        ):
            # The symbol is an already-instantiated class, like a component,
            # which has a __call__.
            vdom = callable_
        else:
            registration = Registration(
                implementation=callable_,
            )
            vdom = inject_callable(
                registration,
                props=full_props,
                registry=registry,
            )

    if callable(vdom):
        # This is class-based component.
        vdom = vdom()

    return vdom


def render(
    value: VDOM,
    registry: Optional[Registry] = None,
    **kwargs,
) -> str:
    """Render a VDOM to a string."""
    return "".join(
        render_gen(
            value,
            registry=registry,
            children=None,
        )
    )


def render_gen(
    value,
    registry: Optional[Registry] = None,
    children=None,
):
    """Render as a generator."""
    for item in flatten(value):
        if isinstance(item, VDOMNode):
            this_tag, props, children = item.tag, item.props, item.children

            # Is this_tag a callable component, or just '<div>'?
            if callable(this_tag):
                yield from render_gen(
                    relaxed_call(this_tag, registry, children=children, props=props)
                )
                continue

            yield f"<{escape(this_tag)}"
            if props:
                pi = props.items()
                yield f" {' '.join(encode_prop(k, v) for (k, v) in pi)}"

            if children:
                yield ">"
                yield from render_gen(children, registry)
                yield f"</{escape(this_tag)}>"
            elif this_tag.lower() in VOIDS:
                yield "/>"
            else:
                yield f"></{this_tag}>"
        elif item not in (True, False, None):
            yield escape(item)


def encode_prop(k, v):
    """If possible, reduce an attribute to just the name."""
    if v is True:
        return escape(k)
    return f'{escape(k)}="{escape(v)}"'


# #########
# The Context API is currently unused. It will be replaced later
# with a non-threadlocal implementation in the switch to asyncio.


_local = threading.local()


def Context(children=None, **kwargs):  # noqa: N802
    """Like the React Conext API."""
    context = getattr(_local, "context", ChainMap())
    try:
        _local.context = context.new_child(kwargs)
        yield children
    finally:
        _local.context = context


def use_context(key, default=None):
    """Similar to the React use context API."""
    context = getattr(_local, "context", ChainMap())
    return context.get(key, default)
