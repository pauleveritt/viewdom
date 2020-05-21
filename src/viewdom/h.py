import threading
from collections import namedtuple, ChainMap
from collections.abc import Iterable, ByteString
from inspect import signature, Parameter

from markupsafe import escape
from htm import htm

H = namedtuple("H", ["tag", "props", "children"])

html = htm(H)


def flatten(value):
    if isinstance(value, Iterable) and not isinstance(value, (H, str, ByteString)):
        for item in value:
            yield from flatten(item)
    else:
        yield value


def relaxed_call(callable_, **kwargs):
    sig = signature(callable_)
    parameters = sig.parameters

    if not any(p.kind == p.VAR_KEYWORD for p in parameters.values()):
        extra_key = "_"
        while extra_key in parameters:
            extra_key += "_"

        sig = sig.replace(
            parameters=[*parameters.values(), Parameter(extra_key, Parameter.VAR_KEYWORD)])
        kwargs = dict(sig.bind(**kwargs).arguments)
        kwargs.pop(extra_key, None)

    return callable_(**kwargs)


def render(value, **kwargs):
    return "".join(render_gen(Context(value, **kwargs)))


def render_gen(value):
    for item in flatten(value):
        if isinstance(item, H):
            tag, props, children = item
            if callable(tag):
                yield from render_gen(relaxed_call(tag, children=children, **props))
                continue

            yield f"<{escape(tag)}"
            if props:
                yield f" {' '.join(encode_prop(k, v) for (k, v) in props.items())}"

            if children:
                yield ">"
                yield from render_gen(children)
                yield f'</{escape(tag)}>'
            else:
                yield f'/>'
        elif item not in (True, False, None):
            yield escape(item)



def encode_prop(k, v):
    if v is True:
        return escape(k)
    return f'{escape(k)}="{escape(v)}"'


_local = threading.local()


def Context(children=None, **kwargs):
    context = getattr(_local, "context", ChainMap())
    try:
        _local.context = context.new_child(kwargs)
        yield children
    finally:
        _local.context = context


def use_context(key, default=None):
    context = getattr(_local, "context", ChainMap())
    return context.get(key, default)
