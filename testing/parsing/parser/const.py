from __future__ import annotations

from typing import Generic, TypeVar

from valtypes.parsing.parser import ABC

__all__ = ["Const"]


T = TypeVar("T")


class Const(ABC[object, T], Generic[T]):
    def __init__(self, value: T):
        self._value = value

    def parse(self, source: object, /) -> T:
        return self._value

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Const):
            return self._value == other._value
        return NotImplemented
