from __future__ import annotations

from valtypes.typing import GenericAlias

from .resolve_type_args import resolve_type_args
from .suppress_slots_meta import SuppressSlotsMeta

__all__ = [
    "SuppressSlotsMeta",
    "pretty_type_repr",
    "resolve_type_args",
]


def pretty_type_repr(type_: object, /) -> str:
    if isinstance(type_, GenericAlias):
        return pretty_type_repr(type_.__origin__) + "[" + ", ".join(pretty_type_repr(arg) for arg in type_.__args__) + "]"
    if isinstance(type_, type):
        return type_.__name__
    return repr(type_)
