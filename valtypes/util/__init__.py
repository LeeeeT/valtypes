from __future__ import annotations

import inspect
from collections.abc import Iterable
from itertools import zip_longest
from typing import TypeVar

from regex import Match, Pattern

from valtypes.typing import HasModuleAndName

from .resolve_type_args import resolve_type_args
from .suppress_slots_meta import SuppressSlotsMeta

__all__ = [
    "resolve_type_args",
    "SuppressSlotsMeta",
    "get_caller_namespace",
    "get_absolute_name",
    "strict_match",
    "iterate_in_parallel",
]


T = TypeVar("T")


def get_caller_namespace() -> dict[str, object]:
    frame = inspect.stack()[2][0]
    return frame.f_builtins | frame.f_globals | frame.f_locals


def get_absolute_name(obj: HasModuleAndName, /) -> str:
    return f"{obj.__module__}.{obj.__name__}"


def strict_match(pattern: Pattern[str], string: str) -> Match[str]:
    match = pattern.fullmatch(string)
    if match is None:
        raise ValueError
    return match


MISSING = object()


def iterate_in_parallel(*iterables: Iterable[T]) -> Iterable[T]:
    for values in zip_longest(*iterables, fillvalue=MISSING):
        for value in values:
            if value is not MISSING:
                yield value
