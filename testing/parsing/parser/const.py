from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar

from valtypes.parsing.parser import ABC

__all__ = ["Const"]


T = TypeVar("T")


@dataclass(init=False, repr=False)
class Const(ABC[object, T]):
    _value: T

    def __init__(self, value: T):
        self._value = value

    def parse(self, source: object, /) -> T:
        return self._value
